#!/usr/bin/env python

from distutils.core import setup

from os.path import abspath, dirname, join
execfile(join(dirname(abspath(__file__)), 'src', 'JsonLibrary', 'version.py'))

DESCRIPTION = ""


CLASSIFIERS = ""

setup(name         = 'robotframework-jsonlib',
      version      = VERSION,
      description  = 'Robot Framework keyword library wrapper around json',
      long_description = DESCRIPTION,
      author       = 'Jingang Song',
      author_email = 'soukingang@gmail.com',
      url          = 'http://github.com/soukingang/robotframework-jsonlib',
      license      = 'Public Domain',
      keywords     = 'robotframework testing test automation json',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = ['JsonLibrary'],
      package_data = {'JsonLibrary': ['tests/*.txt']},
      install_requires=[
          'robotframework',
          'demjson',
          'paramiko'
      ],
)
