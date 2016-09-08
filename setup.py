#!/usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

twisted_deps = ['twisted']

setup(
    name = 'voltha',
    version = '0.0.1',
    author = 'Zsolt Haraszti, Nathan Knuth, Ali Al-Shabibi',
    author_email = 'zharaszt@ciena.com',
    description = ('Virtual Optical Line Terminal (OLT) Hardware Abstraction'),
    license = 'LICENSE.txt',
    keywords = 'volt gpon cord',
    url = 'http://gerrit.opencord.org/voltha',
    packages=['voltha', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Networking',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache License 2.0',
    ],
    install_requires=['siz>1.7.2'],
    extras_require={
        'twisted': twisted_deps,
        'all' : twisted_deps
    },
)
                                        
