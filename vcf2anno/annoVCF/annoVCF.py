# cofing:utf-8
'''import os,sys
from config import annovar
class Anno:
    
    def __init__(self,avinput,db,species,prefix):
        self.species = species
		self.avinput = avinput

    def gene_based(self):
		annovar = 
		cmd = "%s -out %s -build hg19 %s %s" % (annovar,inputfl,outfl,db)#table_annovar.pl
		os.sys(cmd)

    def region_based(self):
        pass

    def filter_based(self):
        pass
'''

import sys
from config import table_annovar,anno_db
import os

class AnnoVCF:
		
	def __init__(self,avinput,species,prefix,db=None):
		self.avinput = avinput
		self.species = species
		self.prefix = prefix
		self.db = db
		self.db_path = os.path.join(anno_db,self.species)

	def gene_based(self):
		genedb = os.path.join(self.db_path,"gene_based")
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, genedb)
		prodb_list = []
		for dbfile in os.listdir(genedb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				prodb_list.append(prodb)
		cmd += ','.join(prodb_list)
		cmd += ' -operation '+','.join(['g']*len(prodb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Genebased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.GeneBased.' + self.species + '_multianno.txt'
		return outFile
	
	def region_based(self):
		regiondb = os.path.join(self.db_path,"region_based")
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, regiondb)
		prodb_list = []
		for dbfile in os.listdir(regiondb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				prodb_list.append(prodb)
		cmd += ','.join(prodb_list)
		cmd += ' -operation '+','.join(['r']*len(prodb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Regionbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.RegionBased.' + self.species + '_multianno.txt'
		return outFile


	def filted_based(self):
		filterdb = os.path.join(self.db_path,"filter_based")
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species,filterdb)
		prodb_list = []
		for dbfile in os.listdir(filterdb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				prodb_list.append(prodb)
		cmd += ','.join(prodb_list)
		cmd += ' -operation '+','.join(['f']*len(prodb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Filterbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.FilterBased.' + self.species + '_multianno.txt'
		return outFile


