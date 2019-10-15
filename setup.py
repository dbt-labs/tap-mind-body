#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-mind-body',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Mind Body API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_mind_body'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      entry_points='''
          [console_scripts]
          tap-mind-body=tap_mind_body:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_mind_body': [
              'schemas/*.json'
          ]
      })