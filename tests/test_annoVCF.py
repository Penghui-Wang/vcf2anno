#python
import sys
sys.path.append("../")
from vcf2anno.config import human_db,table_annovar,anno_db
from vcf2anno.annoVCF.annoVCF import AnnoVCF

prefix = "testannovcf"
species = "hg19"
avinput = "mutect.avinput"
db = "/lustre/common/softs/public/annovar/humandb/hg19_clinvar.txt"
test = AnnoVCF(avinput,db,species,prefix)
testgenebase = test.gene_based()
testrgbase = test.region_based()
testfilbase = test.filted_based()
print testgenebase, testrgbase, testfilbase

