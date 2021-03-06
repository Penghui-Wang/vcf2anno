#!/usr/bin/env python
#coding: utf-8

from setuptools import setup

setup(
    name = 'vcf2anno',
    version = '0.1',
    author = 'wph',
    author_email = 'wangpenghui@gene.ac',
    url = 'https://github.com/Penghui-Wang/vcf2anno',
    description = 'annovcf',
    packages = ['vcf2anno'],
    install_requires = [],
    entry_points = {
        'console_scripts':[
            'anno = test_for_travis:AnnoVCF',
            'fmt = test_for_travis:fmtVCF'
        ]
       }
)
