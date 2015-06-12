#!/usr/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'nose',
    'alembic',
    'sqlalchemy',
    'psycopg2',
    'geoalchemy2',
    'pyramid'
]

config = {
    'description': 'Geographic information for Lightbase',
    'long_description': README + '\n\n' + CHANGES,
    'keywords': 'web postgis',
    'classifiers': [
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    'author': 'Eduardo F. Santos',
    'url': 'http://www.lightbase.com.br',
    'download_url': 'http://github.com/lightbase/LBGeo',
    'author_email': 'eduardo@eduardosan.com',
    'version': '0.5',
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': requires,
    'tests_require': requires,
    'packages': find_packages(),
    'scripts': [
    ],
    'test_suite': 'lbgeo',
    'name': 'LBGeo',
    'entry_points': """\
      [paste.app_factory]
      main = lbgeo:main
      """,
}

setup(**config)
