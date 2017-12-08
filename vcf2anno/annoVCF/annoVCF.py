import os,sys
from config import annovar
class Anno:
    
    def __init__(self,avinput,species,prefix):
        self.species = species
		self.avinput = avinput

    def gene_based(self):
		annovar = 
		cmd = "%s -out %s -build hg19 %s %s" % (annovar,inputfl,outfl,db)#table_annovar.pl处理多种库
		os.sys(cmd)

    def region_based(self):
        pass

    def filter_based(self):
        pass
