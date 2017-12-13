#coding:utf-8
import os
vcf2anno = "/lustre/users/wangpenghui/DevWork/vcf2anno/bin/vcf2anno.py"
vcf = "mutect.varscan.germline.snp.vcf"
dbpath = "/lustre/users/yangrui/anno_db/hg19"
prefix = "22"
cmd = "python %s -i %s -db %s -p %s" % (vcf2anno,vcf,dbpath,prefix)
os.system(cmd)
