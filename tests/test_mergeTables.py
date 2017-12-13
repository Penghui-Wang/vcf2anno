import sys
sys.path.append("../")
from vcf2anno.annoVCF.mergeTables import mergeTables

prefix = "infoandanno"
file_list = ["mutect.vars.info","testannovcf.Genebased.hg19_multianno.txt","testannovcf.Regionbased.hg19_multianno.txt","testannovcf.Filterbased.hg19_multianno.txt"]
merge = mergeTables(prefix,file_list)
print merge
