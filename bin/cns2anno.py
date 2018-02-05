#!/bin/python2.7
#coding:utf-8
__author__ = 'PH.Wang'

import sys,os
import argparse
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
vcfpath = os.path.join(absdir,'../vcf2anno')
sys.path.append(vcfpath)
from annoVCF.annoCNV import cns2anno,annoVCF,formatAnnoResult,del_anresult

def cnsanno(cns,prefix):
    avi = cns2anno(cns,prefix)
    anno = annoVCF(avi,prefix)
    result = formatAnnoResult(avi,anno,prefix)
    del_anresult(anno)
    return result


if __name__ == '__main__':
    usage = '''
Usage:
    annoCNV.py -i <cnsinput> -p <prefix>
    annoCNV.py -h | --help
    annoCNV.py -v | --version

Options:
    -h --help                         print usage
    -v --version                      print version information
    -i <cnsinput> --input <cnsinput>  input cnsfile
    -p <prefix> --pref <prefix>       output prefix
'''
    from docopt import docopt
    args = docopt(usage)
    filename = args["--input"]
    prefix = args["--pref"]
    result = cnsanno(filename,prefix)

