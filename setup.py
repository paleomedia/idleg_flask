#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
  name = 'idleg',
  version='1.0',
  license='GNU General Public License v3',
  author='Nathaniel Hoffman',
  author_email='nathaniel.hoffman@gmail.com',
  description='Idleg application for Flask',
  packages=['app', 'app.auth', 'app.idleg'],
  include_package_data=True,
  zip_safe = False,
  platforms='any',
  install_requires=['flask',],
  classifiers=['Development Status :: 4 - Beta','Environment :: Web Environment',
  'Intended Audience :: Developers','License :: OSI Approved :: GNU General Public License v3','Operating System :: OS Independent',
  'Programming Language :: Python',
  'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  'Topic :: Software Development :: Libraries :: Python Modules'],)
