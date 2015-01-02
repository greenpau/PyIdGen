#   Copyright (C) 2014 Paul Greenberg <paul@greenberg.pro>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from codecs import open
from os import path

pkg_dir = path.abspath(path.dirname(__file__));
pkg_name = 'PyIdGen';
pkg_ver = '1.1';
pkg_url = 'https://github.com/greenpau/' + pkg_name;
pkg_download_url = 'https://pypi.python.org/packages/source/P/PyIdGen/' + pkg_name + '-' + pkg_ver + '.tar.gz#md5=6b3c52d82ba882732b234a1232e358f6';

with open(path.join(pkg_dir, 'README.rst'), encoding='utf-8') as f:
    pkg_long_description = f.read();

setup(
    name=pkg_name,
    version=pkg_ver,
    description='User Profile Generation Library for Quality Assurance and Information Security Testing',
    long_description=pkg_long_description,
    url=pkg_url,
    download_url=pkg_download_url,
    author='Paul Greenberg',
    author_email='paul@greenberg.pro',
    license='GPLv3',
    platform='*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    packages=['pyidgen'],
)
