#python
import sys
sys.path.append("../")
from vcf2anno.config import human_db,table_annovar,anno_db
from vcf2anno.annoVCF.annoVCF import AnnoVCF

anno_db = "/lustre/users/yangrui/anno_db"
dbpath = "/lustre/users/yangrui/anno_db/hg19"
prefix = "multianndb"
species = "hg19"
avinput = "mutect.avinput"
db = ['tfbsConsSites','clinvar']
test = AnnoVCF(avinput,dbpath,prefix)
testgenebase = test.gene_based()
#testrgbase = test.region_based()#complete
#testfilbase = test.filter_based()#complete
#testselectdb = test.single_db() #complete
#testall = test.anno_alldb()#complete
#testmultidb = test.anno_multidb(db)#complete
print testgenebase#, testrgbase, testfilbase
#print testselectdb
#print testall
#print testmultidb
