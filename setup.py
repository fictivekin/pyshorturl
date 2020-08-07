
""" Install script for pyShortUrl """

import os
from setuptools import setup

from pyshorturl.conf import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyShortUrl",
    version = VERSION,
    author = "Fictive Kin (mostly of previous work by Parth Bhatt)",
    author_email = "systems@fictivekin.com",
    description = ("A python library to shorten urls using one of the url shortening services"),
    license = "MIT",
    keywords = "url shortening qrcode qr goo.gl bit.ly tinyurl.com j.mp bitly.com v.gd is.gd",
    platforms = ['Linux', 'Max OS X', 'Windows', 'BSD', 'Unix'],
    url = "https://github.com/fictivekin/pyshorturl",
    data_files=[
        ('.', ['README.rst']),
      ],
    packages = ['pyshorturl', 'pyshorturl/providers'],
    long_description = read('README.rst'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=[
        "requests"
    ],
)
