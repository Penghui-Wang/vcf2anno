import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoVCF import InfoVCF


vcf = "/lustre/users/yangrui/devwork/fastq2vcf/tests/mutect.freebayes.vcf"
prex = "mutect.freebayes"

iv = InfoVCF(vcf,prex)
iv.get_vcf_info()
