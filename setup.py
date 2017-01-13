#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pretty_exceptions',
    version='0.1.0',
    description="Pretty prints exception info in html/pdf",
    long_description=read('README.md'),
    author="Damodharan Thulasiram",
    author_email="thulasi503@gmail.com",
    url='www.gitlab.com/',
    install_requires=read('requirements.txt'),
    license=read('LICENSE'),
    packages=find_packages(exclude=('tests', 'docs')),
)
