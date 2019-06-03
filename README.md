# EDSM BigQuery Loader
This project is an attempt at loading galaxy data from Elite Dangerous into
Google BigQuery for bulk analysis.  And to find Raxxla, of course.

Utilizes the Apache Beam SDK and Google Cloud Dataflow to ensure files can be
processed quickly.  Benchmarked at <15 minutes for BigQuery ingestion.

## Installation instructions
Meant to run on Mac or Linux, untested on Windows.  Python 2 due to Apache Beam
SDK requirements.

1. pip install -r requirements.txt
2. If you encounter GCloud version collisions, 'pip install 
   apache-beam[gcp] google-cloud-storage' should work just as well.
3. chmod +x beam_parser.py
4. ./beam_parser.py --help

## Usage
This pipeline depends heavily on Google Cloud services.  Ensure you are
[properly authenticated](https://cloud.google.com/docs/authentication/) before
running.

### Download EDSM files
This will download files to /tmp/ on your local machine.  Ensure you have enough
space to store these files, they're well over 100 GB in total.

```./beam_parser.py --download powerplay```


### Stage EDSM files on Google Cloud Storage
This will stage locally downloaded files onto Google Cloud Storage.  If you want
to use Google Cloud Dataflow, you will need to do this to ensure the Dataflow
runner has access to the file.  The Dataflow runner is significantly faster than
the Direct runner, so this is highly recommended.

```./beam_parser.py --project <project id> --bucket <bucket id> --upload_to_gcs powerplay```


### Run Google Cloud Dataflow
This will process the files staged on GCS and load them into BigQuery.  The
destination BigQuery dataset must be created before running this command.

```./beam_parser.py --project <project id> --bucket <bucket id> --dataset <dataset id> --runner DataflowRunner --upload_to_bq powerplay```
