#!/bin/python2.7
#coding:utf-8
__author__ = 'PH.Wang'

import sys,os
import argparse
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
vcfpath = os.path.join(absdir,'../vcf2anno')
sys.path.append(vcfpath)

from fmtVCF.fmtVCF import fmtVCF
from infoVCF.infoVCF import InfoVCF
from annoVCF.annoVCF import AnnoVCF
from annoVCF.mergeTables import mergeTables

'''
	Add the needed parmeter
'''
parser = argparse.ArgumentParser()
parser.add_argument('--inputvcf','-i',help ='input vcf file' )
parser.add_argument('--dbpath','-db',help = 'path of all the database')
parser.add_argument('--prefix','-p',help = 'prefix')
parser.parse_args()

def vcf2anno(vcf,dbpath,prefix):
	fvcf = fmtVCF(vcf,prefix)
	iv = InfoVCF(fvcf,prefix)
	avinput,invcf = iv.get_vcf_info()
	anvcf = AnnoVCF(avinput,dbpath,prefix)
	genebase_out = anvcf.gene_based()
	regionbase_out = anvcf.region_based()
	filterbase_out = anvcf.filter_based()
	file_list = [invcf,genebase_out,regionbase_out,filterbase_out]
	xls = mergeTables(prefix,file_list)
	return xls


if __name__ == "__main__":
	if len(sys.argv) is 1:
		parser.print_help()
	else:
		parmet = parser.parse_args(sys.argv[1:])
		anvcf = vcf2anno(parmet.inputvcf,parmet.dbpath,parmet.prefix)
		print anvcf
	

