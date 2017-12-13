#coding: utf-8

class InfoVCF(object):
	def __init__(self,vcf,prefix):
		self.vcf = vcf
		self.prefix = prefix

	def get_vcf_info(self):
		lines = open(self.vcf).readlines()
		out = self.prefix + ".vars.info"
		avi = self.prefix + ".avinput"
		fho = open(out,'w')
		fha = open(avi,'w')
		head = "\t".join(['Chr','Start','End','Ref','Alt','Read1','Read2','VarFreq','Strand1','Strand2','Qual','Qual1','Qual2','Pvalue','MapQual1','MapQual2','Read1plus','Read1minus','Read2plus','Read2minus','Zygosity','Cons','VarType','Depth']) + "\n"
		fho.write(head)
		for line in lines:
			line = line.strip("\n")
			if line.startswith("#"):
				continue
			items = line.split('\t')
			chrom, start, ref, alt = items[0], items[1], items[3], items[4]
			end = str(int(start)+len(ref)-1)
			qual, infostr, formatstr, samplestr = items[5], items[7],items[8],items[9]
			info_dict = self.get_format_info(infostr,formatstr,samplestr)
			vartype = self.getVartype(ref,alt)
			reads1 = self.getReads1(info_dict)
			reads2 = self.getReads2(info_dict)
			dep = self.getDepth(info_dict)
			genotype = self.getGenoType(info_dict)
			r1plus = self.getReads1plus(info_dict)
			r1minus = self.getReads1minus(info_dict)
			r2plus = self.getReads2plus(info_dict)
			r2minus = self.getReads2minus(info_dict)
			strand1 = self.getStrand1(r1plus,r2plus)
			strand2 = self.getStrand2(r1minus,r2minus)
			varfreq = self.getVarFreq(info_dict,dep,reads2)
			cons = self.getCons()
			qual1 = self.getQual1(info_dict)
			qual2 = self.getQual2(info_dict)
			pvalue = self.getPvalue(info_dict)
			mapq1 = self.getMapqual1(info_dict)
			mapq2 = self.getMapqual2(info_dict)
			
			outline = "\t".join([chrom,start,end,ref,alt,reads1,reads2,varfreq,strand1,strand2,qual,qual1,qual2,pvalue,mapq1,mapq2,r1plus,r1minus,r2plus,r2minus,genotype,cons,vartype,dep]) + "\n"
			fho.write(outline)
			aviline = "\t".join([chrom,start,end,ref,alt]) + "\n"
			fha.write(aviline)
			
			
		fho.close()
		fha.close()
		return avi,out

	def get_format_info(self,infostr,formatstr,samples):		
		info_dict = {}
		infoitems = infostr.split(";")
		for it in infoitems:
			try:
				k,v = it.split("=")
				info_dict[k] = v
			except:
				break
		format_list = formatstr.split(":")
		sample_list = samples.split(":")
		for i in range(len(format_list)):
			info_dict[format_list[i]] = sample_list[i]
		return info_dict

	def getCons(self):
		cons = ''
		return cons
 
	def getVartype(self,ref,alt):
		if ref == '-':
			vartype = "ins"
		elif len(ref) == 1:
			if alt == '-':
				vartype = "del"
			elif len(alt) == 1:
				vartype = "snp"
			else:
				vartype = "sub"
		else:
			if alt == '-':
				vartype = "del"
			elif len(ref) == len(alt):
				vartype = "mnp"
			else:
				vartype = "sub"
		return vartype


	def getReads1(self,info_dict):
		read1 = ''
		read1name = ['RD','RO','AD']#RD在AD前（子情况在前）
		for key in read1name:
			if key in info_dict:
				read1 = info_dict[key]
				break
		if "," in read1:
			read1 = read1.split(",")[0]
		return read1
	
	def getReads2(self,info_dict):
		read2name = ['AO','AD']#AD情况较多放后面，避免多次赋值
		read2 = ''
		for key in read2name:
			if key in info_dict:
				read2 = info_dict[key]
				break
		if "," in read2:
			read2 = read2.split(",")[1]
		return read2
	
	def getDepth(self,info_dict):
		depth = ''
		Depthname = ['DP']
		for key in Depthname:
			if key in info_dict:
				depth = info_dict[key]
				break
		return depth

	
	def getGenoType(self,info_dict):
		genotype = ''
		Gtname = ['GT']
		for key in Gtname:
			if key in info_dict:
				Gt = info_dict[key]
				break
		if Gt.split('/')[0] == Gt.split('/')[1]:
			genotype = 'Homozygous'
		else:
			genotype = 'Heterozygous'
		return genotype
	
	def getReads1plus(self,info_dict):
		read1plus = ''
		read1plusname = ['RDF','SRF']
		for key in read1plusname:
			if key in info_dict:
				read1plus = info_dict[key]
				break
		return read1plus

	def getReads1minus(self,info_dict):
		read1minus = ''
		read1minusname = ['RDR','SRR']
		for key in read1minusname:
			if key in info_dict:
				read1minus = info_dict[key]
				break
		return read1minus
	
	def getReads2plus(self,info_dict):
		read2plus = ''
		read2plusname = ['ADF','SAF']
		for key in read2plusname:
			if key in info_dict:
				read2plus = info_dict[key]
				break
		return read2plus

	def getReads2minus(self,info_dict):
		read2minus = ''
		read2minusname = ['ADR','SAR']
		for key in read2minusname:
			if key in info_dict:
				read2minus = info_dict[key]
				break
		return read2minus


	def getStrand1(self,read1plus,read2plus):
		strand1 = ''
		if read1plus and read2plus:
			if "," in read1plus or "," in read2plus:
				pass
			else:
				r1p = int(read1plus)
				r2p = int(read2plus)
				strand1 = str(r1p + r2p)
		
		return strand1


	def getStrand2(self,read1minus,read2minus):
		strand2 = ''
		if read1minus and read2minus:
			if "," in read1minus or "," in read2minus:
				pass
			else:
				r1m = int(read1minus)
				r2m = int(read2minus)
				strand2 = str(r1m + r2m)
		return strand2

	def getQual1(self,info_dict):
		qual1 = ''
		qual1name = ['RBQ','QR']
		for key in qual1name:
			if key in info_dict:
				qual1 = info_dict[key]
				break
		return qual1
	
	def getQual2(self,info_dict):
		qual2 = ''
		qual2name = ['ABQ','QA']
		for key in qual2name:
			if key in info_dict:
				qual2 = info_dict[key]
				break
		return qual2
	
	def getVarFreq(self,info_dict,depth,read2):#有值直接提取，没有再计算
		varfreq = ''
		varfreqname =['FREQ']
		for key in varfreqname:
			if key in info_dict:
				varfreq = info_dict[key]
				break
			elif read2:
				try:
					varfreq = str(round(float(read2)/float(depth),4)*100) + '%'
				except:
					pass
		return varfreq

	def getPvalue(self,info_dict):
		pvalue = ''
		pvaluename = ['FS','PVAL']
		for key in pvaluename:
			if key in info_dict:
				pvalue = info_dict[key]
				break
		return pvalue
	
	def getMapqual1(self,info_dict):
		mapqual1 = ''
		mapquanl1name = ['MQ','MQMR']
		for key in mapquanl1name:
			if key in info_dict:
				mapqual1 = info_dict[key]
				break
		return mapqual1

	def getMapqual2(self,info_dict):
		mapqual2 = ''
		mapqual2name =['MQM'] 
		for key in mapqual2name:
			if key in info_dict:
				mapqual2 = info_dict[key]
				break
		return mapqual2



"""
if __name__ == '__main__':
	import sys
	vcf = sys.argv[1]
	prefix = sys.argv[2]	
	iv = InfoVCF(vcf, prefix)
	iv.get_vcf_info()
"""

