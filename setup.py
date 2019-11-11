#!/usr/bin/env python
import io
import os

from setuptools import find_packages, setup

# package meta data
NAME = 'textformatting'
DESCRIPTION = 'A Japanese text formatter'
EMAIL = 'contact@nlp.ist.i.kyoto-u.ac.jp'
AUTHOR = 'Kurohashi-Kawahara Lab, Kyoto University'
VERSION = ''

INSTALL_REQUIRES = []

SETUP_REQUIRES = [
    'pytest-runner'
]

TEST_REQUIRES = [
    'pytest==4.6.5'
]

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with io.open(os.path.join(here, NAME, '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(exclude=('tests',)),
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ]
)
