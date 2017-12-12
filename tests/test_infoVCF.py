import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoVCF import InfoVCF


vcf = "mutect.freebayes.breakmulti.vcf"
prex = "mutect"

iv = InfoVCF(vcf,prex)
iv.get_vcf_info()
