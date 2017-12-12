# cofing:utf-8

import sys
from config import table_annovar
import os

class AnnoVCF:
		
	def __init__(self,avinput,species,anno_db,prefix):
		self.avinput = avinput
		self.species = species
		self.prefix = prefix
		self.db_path = os.path.join(anno_db,self.species)
		self.genedb = os.path.join(self.db_path,"gene_based")
		self.regiondb = os.path.join(self.db_path,"region_based")
		self.filterdb = os.path.join(self.db_path,"filter_based")
		self.genedb_list = []
		self.regiondb_list = []
		self.filterdb_list = []
		for dbfile in os.listdir(self.genedb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				self.genedb_list.append(prodb)
		for dbfile in os.listdir(self.regiondb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				self.regiondb_list.append(prodb)
		for dbfile in os.listdir(self.filterdb):
			if os.path.splitext(dbfile)[1] == ".txt":
				prodb = dbfile.split(self.species+'_')[-1].split(".")[0]
				self.filterdb_list.append(prodb)


	def gene_based(self):
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, self.genedb)
		cmd += ','.join(self.genedb_list)
		cmd += ' -operation '+','.join(['g']*len(self.genedb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Genebased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Genebased.' + self.species + '_multianno.txt'
		return outFile
	
	def region_based(self):
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, self.regiondb)
		cmd += ','.join(self.regiondb_list)
		cmd += ' -operation '+','.join(['r']*len(self.regiondb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Regionbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Regionbased.' + self.species + '_multianno.txt'
		return outFile


	def filter_based(self):
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species,self.filterdb)
		cmd += ','.join(self.filterdb_list)
		cmd += ' -operation '+','.join(['f']*len(self.filterdb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Filterbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Filterbased.' + self.species + '_multianno.txt'
		return outFile


	def anno_multidb(self,db_list):
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species,self.db_path)
		ope_list = []
		for i in range(len(self.db)):
			if db_list[i] in self.genedb_list:
				ope_list.append('g')
			elif db_list[i] in self.regiondb_list:
				ope_list.append('r')
			elif db_list[i] in self.filterdb_list:
				ope_list.append('f')
			else:
				print "Input error or the query database does not exist"
		cmd += ','.join(db_list)
		cmd += ' -operation '+','.join(ope_list)
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.multianno')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.multianno' + self.species + '_multianno.txt'
		return outFile



