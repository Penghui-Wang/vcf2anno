import sys
sys.path.append("../")
from vcf2anno.fmtVCF.fmtVCF import fmtVCF

vcf = "/home/testData/vcf2anno/test.freebayes.vcf"
prex = "22"

fmtVCF(vcf,prex) 
