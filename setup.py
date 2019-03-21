# -*- coding: utf-8 -*-
#
# This file is part of the python-shogi library.
# Copyright (C) 2012-2014 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>
# Copyright (C) 2015- Tasuku SUENAGA <tasuku-s-github@titech.ac>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import io
import shogi
import setuptools
from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

if USE_CYTHON:
    ext = '.pyx'
    cmdclass = {'build_ext': build_ext}
else:
    ext = '.c'
    cmdclass = {}

ext_modules = [
    Extension('shogi.Init', sources=['shogi/Init' + ext]),
    Extension('shogi.Consts', sources=['shogi/Consts' + ext]),
    Extension('shogi.CSA', sources=['shogi/CSA' + ext]),
    Extension('shogi.KIF', sources=['shogi/KIF' + ext]),
    Extension('shogi.Move', sources=['shogi/Move' + ext]),
    Extension('shogi.Person', sources=['shogi/Person' + ext]),
    Extension('shogi.Piece', sources=['shogi/Piece' + ext])
]

def read_description():
  description = io.open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8').read()
  return description

setup(
    name = 'python-shogi',
    version = shogi.__version__,
    author = shogi.__author__,
    author_email = shogi.__email__,
    description = 'A pure Python shogi library with move generation and validation and handling of common formats.',
    long_description = read_description(),
    license = "GPL3",
    keywords = 'shogi csa kif',
    url = 'https://github.com/gunyarakun/python-shogi',
    packages = ['shogi'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    scripts = [],
    test_suite = 'nose.collector',
    tests_require = ['nose>=1.0', 'mock'],
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Topic :: Games/Entertainment :: Board Games',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
