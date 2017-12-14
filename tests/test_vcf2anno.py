#coding:utf-8
import os

def test_vcf2anno():
	vcf2anno = "/lustre/users/wangpenghui/DevWork/vcf2anno/bin/vcf2anno.py"
	vcf = "data/mutect.varscan.germline.snp.vcf"
	dbpath = "/lustre/users/yangrui/anno_db/hg19"
	prefix = "data/22"
	cmd = "python %s -i %s -db %s -p %s" % (vcf2anno,vcf,dbpath,prefix)
	print cmd
	status = os.system(cmd)
	assert status != None

