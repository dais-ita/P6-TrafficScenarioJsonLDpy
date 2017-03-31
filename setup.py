# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CameraJsonLD',
    version='0.0.1',
    description='JsonLD facilities for T6.2 Camera Scenario',
    long_description=readme,
    author='Federico Cerutti',
    author_email='federico.cerutti@acm.org',
    url='https://dais-ita.org',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

