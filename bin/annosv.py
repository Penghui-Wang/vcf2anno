#!/bin/python2.7
#coding:utf-8
__author__ = 'PH.Wang'

import sys,os
import argparse
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
vcfpath = os.path.join(absdir,'../vcf2anno')
sys.path.append(vcfpath)
from annoVCF.annoSV import breakdancer2avi,annoVCF,formatAnnoResult

def annoSV(brdancerout,prefix):
	avi = breakdancer2avi(brdancerout,prefix)
	anno = annoVCF(avi,prefix)
	result = formatAnnoResult(avi,anno,prefix)
	return result


if __name__ == '__main__':
	usage = '''
Usage:
    annoSV.py -i <brdancerout> -p <prefix> 
    annoSV.py -h | --help
    annoSV.py -v | --version

Options:
    -h --help                       print usage
    -v --version                    print version information
    -i <brdancerout> --input <brdancerout>  input breakdancer out file
    -p <prefix> --pref <prefix>     output prefix

'''
	from docopt import docopt
	args = docopt(usage)
	bdout = args["--input"]
	prefix = args["--pref"]
	result = annoSV(bdout,prefix)

