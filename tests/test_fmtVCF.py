import sys
sys.path.append("../")
from vcf2anno.fmtVCF.fmtVCF import fmtVCF

vcf = "/lustre/users/yangrui/devwork/fastq2vcf/tests/mutect.freebayes.vcf"
prex = "mutect.freebayes"

fmtVCF(vcf,prex) 
