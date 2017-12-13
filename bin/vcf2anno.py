#coding:utf-8
import sys,os
import argparse

from vcf2anno.fmtvcf import fmtvcf
from vc.....


usage = """
		python vcf2anno.py -i vcf -db dppath -out prefix
	
				--help			-h	usage;
			[Required]
				--input			-i	input vcf file;
				--dbpath		-db	path of all the database;
				--prefix		-p	prefix;
			[Optional]
				--annodb		-ad	wanted annonotaed database


"""
def vcf2anno(vcf,dbpath,prefix):

    fvcf = fmtvcf(vcf,prefix)
    pass

    return xls



if __name__ == "__main__":
    parse_args(sys.argv[1:])
    

