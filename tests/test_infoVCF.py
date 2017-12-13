import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoVCF import InfoVCF


vcf = "mutect.freebayes.breakmulti.vcf"
prex = "returntest"

iv = InfoVCF(vcf,prex)
avi,inv = iv.get_vcf_info()
print avi,inv
