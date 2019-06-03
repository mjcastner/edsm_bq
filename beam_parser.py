#!/usr/bin/env python
from __future__ import absolute_import

import apache_beam as beam
import argparse
import json
import logging
import sys
import urllib

from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from google.cloud import bigquery
from google.cloud import storage
from raxxla_transforms import data_transforms
from raxxla_transforms import table_schemas


# Global vars
logger = logging.getLogger('raxxla_loader')
formatter = '%(asctime)s     %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)
table_list = ['bodies', 'systems', 'powerplay', 'population', 'stations']
arg_list = table_list + ['all']
runner_list = ['DataflowRunner', 'DirectRunner']


# Configure flags
flags = argparse.ArgumentParser(description='Initialize Raxxla BigQuery tables from EDSM data.')
flags.add_argument('--project', help='ID of the Google Cloud project to use.')
flags.add_argument('--dataset', help='Name of the BigQuery dataset to store EDSM data in.')
flags.add_argument('--bucket', help='Name of the GCS bucket to store EDSM data in.')
flags.add_argument('--runner', help='Name of the Beam runner type to use for the pipeline.', choices=runner_list)
flags.add_argument('--upload_to_gcs', help='Upload EDSM files to GCS from local download.', choices=arg_list, nargs='+')
flags.add_argument('--delete', help='Delete tables from BigQuery.', choices=arg_list, nargs='+')
flags.add_argument('--download', help='Download files from EDSM into Google Cloud Storage.', choices=arg_list, nargs='+')
flags.add_argument('--upload_to_bq', help='Write converted values to BigQuery.  Requires files to be staged in GCS.', choices=arg_list, nargs='+')
args = flags.parse_args()


class remove_blank_rows(beam.DoFn):
    def process(self, element):
        if element is not None:
            yield element
        else:
            return


def delete_bq_data(tables, project_id, dataset_id):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    tables = set(tables)
    try:
        for table in tables:
            table_ref = dataset_ref.table(table)
            delete_string = 'Deleted ' + project_id + '.' + dataset_id + '.' + table
            client.delete_table(table_ref)
            logger.info(delete_string)
    except Exception as e:
        delete_error_string = 'Unable to delete EDSM BQ tables: ' + str(e)
        logger.error(delete_error_string)
        sys.exit()


def download_edsm_files(files):
    edsm_urls = {
        'bodies': 'https://www.edsm.net/dump/bodies.json',
        'systems': 'https://www.edsm.net/dump/systemsWithCoordinates.json',
        'powerplay': 'https://www.edsm.net/dump/powerPlay.json',
        'population': 'https://www.edsm.net/dump/systemsPopulated.json',
        'stations': 'https://www.edsm.net/dump/stations.json'
    }

    files = set(files)
    try:
        for file in files:
            dl_string = 'Downloading ' + file + ' file from EDSM...'
            logger.info(dl_string)
            download_url = edsm_urls[file]
            download_path = '/tmp/' + file
            urllib.urlretrieve(download_url, download_path)

    except Exception as e:
        download_error_string = 'Unable to download EDSM files: ' + str(e)
        logger.error(download_error_string)
        sys.exit()


def upload_to_bigquery(files, project_id, dataset_id, bucket_id, runner, pipeline_options):
    files = set(files)

    try:
        for file in files:
            import_string = 'Importing ' + file + ' file into BigQuery...'
            logger.info(import_string)
            
            table_spec = project_id + ':' + dataset_id + '.' + str(file)
            if runner == 'DataflowRunner':
                file_path = 'gs://' + str(bucket_id) + '/' + str(file)
            elif runner == 'DirectRunner':
                file_path = '/tmp/' + str(file)

            with beam.Pipeline(options=pipeline_options) as p:
                json_lines = p | beam.io.ReadFromText(file_path)

                if file == 'bodies':
                    schema = table_schemas.bodies
                    rows = json_lines | beam.Map(data_transforms.transform_bodies)
                elif file == 'systems':
                    schema = table_schemas.systems
                    rows = json_lines | beam.Map(data_transforms.transform_systems)
                elif file == 'powerplay':
                    schema = table_schemas.powerplay
                    rows = json_lines | beam.Map(data_transforms.transform_powerplay)
                elif file == 'population':
                    schema = table_schemas.population
                    rows = json_lines | beam.Map(data_transforms.transform_population)
                elif file == 'stations':
                    schema = table_schemas.stations
                    rows = json_lines | beam.Map(data_transforms.transform_stations)
                
                if schema and rows:
                    bq_loader = rows | beam.ParDo(remove_blank_rows()) | beam.io.WriteToBigQuery(
                        table_spec,
                        schema=schema,
                        write_disposition=beam.io.BigQueryDisposition.WRITE_EMPTY,
                        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                        method='DEFAULT',
                        batch_size=500)
                else:
                    raise Exception('Unable to assemble rows for upload.  Check upstream repo for schema updates.')

    except Exception as e:
        bq_upload_error_string = 'Unable to load EDSM files: ' + str(e)
        logger.error(bq_upload_error_string)
        sys.exit()


def upload_to_gcs(files, project_id, bucket):
    try:
        for file in files:
            blob = bucket.blob(file)
            file_path = '/tmp/' + str(file)
            upload_log_string = 'Uploading ' + file + ' to GCS.' 
            logger.info(upload_log_string)
            blob.upload_from_filename(file_path)
    except Exception as e:
        gcs_upload_error_string = 'Unable to upload EDSM files to GCS: ' + str(e)
        logger.error(gcs_upload_error_string)
        sys.exit()


def main(argv=None):
    parser = argparse.ArgumentParser()
    known_args, pipeline_args = parser.parse_known_args(argv)
    project_id = args.project
    dataset_id = args.dataset
    bucket_id = args.bucket

    if args.delete:
        if 'all' in args.delete:
            delete_bq_data(table_list, project_id, dataset_id)
        else:
            delete_bq_data(args.delete, project_id, dataset_id)

    if args.download:
        if 'all' in args.download:
            download_edsm_files(table_list)
        else:
            download_edsm_files(args.download)

    if args.upload_to_gcs:
        storage_client = storage.Client()

        try:
            gcs_bucket = storage_client.get_bucket(bucket_id)
        except Exception as e:
            logger.warning('GCS bucket not found, creating...')
            gcs_bucket = storage_client.create_bucket(bucket_id)

        if 'all' in args.upload_to_gcs:
            upload_to_gcs(table_list, project_id, gcs_bucket)
        else:
            upload_to_gcs(args.upload_to_gcs, project_id, gcs_bucket)

    if args.upload_to_bq:
        staging_location = '--staging_location=gs://' + bucket_id + '/staging'
        temp_location = '--temp_location=gs://' + bucket_id + '/temp'
    
        pipeline_args.extend([
            '--job_name=raxxla-loader',
            '--setup_file=./setup.py',
            staging_location,
            temp_location,
        ])

        pipeline_options = PipelineOptions(pipeline_args)
        pipeline_options.view_as(SetupOptions).save_main_session = True
        runner = args.runner
        
        if 'all' in args.upload_to_bq:
            upload_to_bigquery(table_list, project_id, dataset_id, bucket_id, runner, pipeline_options)
        else:
            upload_to_bigquery(args.upload_to_bq, project_id, dataset_id, bucket_id, runner, pipeline_options)


if __name__ == '__main__':
  main()
