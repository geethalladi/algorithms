# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.org') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algo',
    version='0.1.0',
    description='Library with basic algorithm implementations',
    long_description=readme,
    author='geethalladi',
    author_email='geethalladi@gmail.com',
    url='https://github.com/geethalladi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
