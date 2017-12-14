import sys
sys.path.append("../")
from vcf2anno.fmtVCF.fmtVCF import fmtVCF

def test_fmtvcf():
	vcf = "/lustre/users/yangrui/devwork/fastq2vcf/tests/mutect.freebayes.vcf"
	prex = "mutect.freebayes"
	fmt = fmtVCF(vcf,prex)
	assert fmt == "mutect.freebayes.left.vcf"

if __name__ == "__main__":
	pytest.test_fmtvcf()
