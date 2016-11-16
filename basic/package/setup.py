#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

def main():
    # setuptools.find_packages()を使って現在のディレクトリにあるPythonパッケージを対象に
    setup(
        name='package001',
        version='1.0',
        description='My First Package001.',
        author='test taro',
        author_email='test.taro@xxxx.gmail.com',
        packages=find_packages(),
        )

if __name__ == '__main__':
    main()
    
