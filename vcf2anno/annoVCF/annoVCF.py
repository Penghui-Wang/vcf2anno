# cofing:utf-8
'''import os,sys
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
'''
import sys
from config import table_annovar,anno_db
import glob
import os

class AnnoVCF:
		
	def __init__(self,avinput,db,species,prefix)
		self.avinput = avinput
		self.species = species
		self.prefix = prefix
		self.db = db
		self.db_path = os.path.join(anno_db,self.species)

	def gene_based(self,select_db = db):
		pass
	
	def region_based(self,select_db = db):
		pass

	def filted_based(self,select_db = db):
		pass

		
