import sys
sys.path.append("../")
from vcf2anno.annoVCF.mergeTables import mergeTables

prefix = "Threebased"
file_list = ["testannovcf.Regionbased.hg19_multianno.txt","testannovcf.Filterbased.hg19_multianno.txt","testannovcf.Genebased.hg19_multianno.txt"]
merge = mergeTables(prefix,file_list)
print merge
