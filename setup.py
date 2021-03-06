# coding: utf-8
from setuptools import setup, find_packages
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


__version__ = "0.0.1"

setup(
    name='slavem',
    version=__version__,
    keywords='slavem',
    description=u'监控全网服务的服务',
    long_description=read("README.md"),

    url='https://github.com/lamter/slavem',
    author='lamter',
    author_email='lamter.fu@gmail.com',

    packages=find_packages(),
    package_data={
        "salvett": ["*.json"],
    },
    install_requires=read("requirements.txt").splitlines(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'],
)
