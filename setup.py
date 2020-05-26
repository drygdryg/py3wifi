# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: drygdryg
:license: MIT
:copyright: (c) 2020 drygdryg
"""

version = '0.0.3'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py3wifi',
    version=version,
    description='Wrapper for 3WiFi Wireless Database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',

    author='drygdryg',
    author_email='drygdryg2014@yandex.com',
    url='https://github.com/drygdryg/py3wifi',
    download_url='https://github.com/drygdryg/py3wifi/archive/v{}.zip'.format(version),

    keywords='wrapper api 3wifi',

    packages=['py3wifi'],
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
        'Environment :: Web Environment'
    ]
)
