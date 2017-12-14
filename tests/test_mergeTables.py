import sys
sys.path.append("../")
from vcf2anno.annoVCF.mergeTables import mergeTables

def test_merge():
	prefix = "data/infoandanno"
	file_list = ["data/mutect.vars.info","data/testannovcf.Genebased.hg19_multianno.txt","data/testannovcf.Regionbased.hg19_multianno.txt","data/testannovcf.Filterbased.hg19_multianno.txt"]
	merge = mergeTables(prefix,file_list)
	assert merge == "data/infoandanno.merged.txt"

if __name__ =="__main__":
	pytest.test_merge()
