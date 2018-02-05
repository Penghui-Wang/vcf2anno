#!/bin/python2.7
#coding:utf-8
__author__ = 'PH.Wang'

import sys,os
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
vcfpath = os.path.join(absdir,'../vcf2anno')
sys.path.append(vcfpath)

from fmtVCF.fmtVCF import fmtVCF
from infoVCF.infoVCF import InfoVCF
from annoVCF.annoVCF import AnnoVCF
from annoVCF.mergeTables import mergeTables

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
    usage = '''
Usage:
    vcf2anno.py -i <vcf> -d <dbpath> -p <prefix>
    vcf2anno.py -h | --help
    vcf2anno.py -v | --version

Options:
    -h --help                       print usage
    -v --version                    print version information
    -i <vcf> --input <vcf>          input vcf file
    -d <dbpath> --dbph <dbpath>     annoed dbpath
    -p <prefix> --pref <prefix>        output prefix
'''

    from docopt import docopt
    args = docopt(usage)
    vcf = args["--input"]
    prefix = args["--pref"]
    dbpath = args["--dbph"]
    result = vcf2anno(vcf,dbpath,prefix)

    

