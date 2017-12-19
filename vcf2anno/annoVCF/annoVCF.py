#!/bin/python2.7
# cofing:utf-8
__author__ = 'PH.Wang'

import sys
from config import table_annovar
import os

class AnnoVCF:
		
	def __init__(self,avinput,dbpath,prefix):

		"""Init annovcf class.

		   Args:

		   avinput(str): the input avi file.

		   prefix(str): the output prefix.

		   Returns:

		   init this class.
		"""

		self.avinput = avinput
		self.species = os.path.split(dbpath)[1]
		self.prefix = prefix
		self.db_path = dbpath
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
		"""Anno the input avifile by gene_based.

		   Returns:

		   outfile(str):gene_based annoed output file.
		"""
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, self.genedb)
		cmd += ','.join(self.genedb_list)
		cmd += ' -operation '+','.join(['g']*len(self.genedb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Genebased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Genebased.' + self.species + '_multianno.txt'
		return outFile

	def region_based(self):
		"""Anno the input avifile by region_based.

           Returns:

           outfile(str):region_based annoed output file.
		"""
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species, self.regiondb)
		cmd += ','.join(self.regiondb_list)
		cmd += ' -operation '+','.join(['r']*len(self.regiondb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Regionbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Regionbased.' + self.species + '_multianno.txt'
		return outFile


	def filter_based(self):
		"""Anno the input avifile by filter_based.

		   Returns:

		   outfile(str):filtered_based annoed output file.
		"""
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species,self.filterdb)
		cmd += ','.join(self.filterdb_list)
		cmd += ' -operation '+','.join(['f']*len(self.filterdb_list))
		cmd += ' -nastring . --outfile %s' % (self.prefix + '.Filterbased')
		print cmd
		os.system(cmd)
		outFile = self.prefix + '.Filterbased.' + self.species + '_multianno.txt'
		return outFile


	def anno_multidb(self,db_list):
		"""Anno the input avifile by different databases.

		   Args:

		   db_list(list): different database.

		   Returns:

		   outfile(str):differentdb_based annoed output file.
		"""
		#all the database should be in the same dictionary and well-classified
		cmd = "%s %s --remove -buildver %s %s -protocol " % (table_annovar, self.avinput,self.species,self.db_path)
		#db_path cotain different databases
		ope_list = []
		for i in range(len(db_list)):
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


