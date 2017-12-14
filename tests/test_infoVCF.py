import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoVCF import InfoVCF

def test_invcf():
	vcf = "data/mutect.freebayes.breakmulti.vcf"
	prex = "data/returntest"
	iv = InfoVCF(vcf,prex)
	avi,inv = iv.get_vcf_info()
	assert avi,inv ==("data/returntest.avinput","data/returntest.vars.info")

if __name__ == "__main__":
	pytest.test_invcf()
