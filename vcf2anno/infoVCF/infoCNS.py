#!/usr/bin/env python
#coding: utf-8
__author__ = 'PH.Wang'

class InfoCNS(object):
	def __init__(self,cns,prefix):
		self.cns = cns
		self.prefix = prefix

	def get_cns_info(self):
		lines = open(self.cns).readlines()
		out = self.prefix + ".cns.info"
		avi = self.prefix + ".avinput"
		fho = open(out,'w')
		fha = open(avi,'w')
		head = "\t".join(['Chr','Start','End','Size','VarType','','Fold_change(log2)','Fold_change','Gene_name','Gene_region']) + "\n"
		fho.write(head)
		for line in lines[1:]:
			line = line.strip("\n")
			items = line.split('\t')
			chrom, start, end, genename = items[0], items[1], items[2], items[3]
			cn,log2 = items[4], items[5]
			ref = '0'
			alt = '0'
			vartype = self.getVartype(cn)
			if vartype == "remove":
				continue
			else:
				fold_change = ''
				gene_region = ''
				size = str(int(end) - int(start))
				outline = "\t".join([chrom,start,end,size,vartype,log2,fold_change,genename,gene_region]) + "\n"
				fho.write(outline)
				aviline = "\t".join([chrom,start,end,ref,alt]) + "\n"
				fha.write(aviline)
				
			
		fho.close()
		fha.close()
		return avi,out

 
	def getVartype(self,cn):
		if cn > 2:
			vartype = "dup"
		elif cn < 2:
			vartype = "del"
		else:
			vartype = "remove"
		return vartype



"""
if __name__ == '__main__':
	import sys
	vcf = sys.argv[1]
	prefix = sys.argv[2]	
	iv = InfoVCF(vcf, prefix)
	iv.get_vcf_info()
"""

