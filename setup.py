import setuptools


REQUIRED_PACKAGES = ['google-cloud-bigquery', 'google-cloud-storage', 'apache-beam[gcp]']

setuptools.setup(
    name='raxxla_transforms',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)