#!/usr/bin/env python
#coding: utf-8
__author__ = 'PH.Wang'

import sys,os
import math

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
        head = "\t".join(['Chr','Start','End','Size','VarType','Fold_change(log2)','Fold_change']) + "\n"
        fho.write(head)
        for line in lines[1:]:
            line = line.strip("\n")
            items = line.split('\t')
            chrom, start, end  = items[0], items[1], items[2],
            log2,cn = items[4], items[5]
            ref = '0'
            alt = '0'
            vartype = self.getVartype(cn)
            if vartype == "remove":
                continue
            else:
                log2 = items[4]
                fold_change = str(math.pow(2,float(log2)))
                size = str(int(end) - int(start) + 1)
                outline = "\t".join([chrom,start,end,size,vartype,log2,fold_change]) + "\n"
                fho.write(outline)
                aviline = "\t".join([chrom,start,end,ref,alt]) + "\n"
                fha.write(aviline)
                
            
        fho.close()
        fha.close()
        return avi,out

 
    def getVartype(self,cn):
        if int(cn) > 2:
            vartype = "dup"
        elif int(cn) < 2:
            vartype = "del"
        else:
            vartype = "remove"
        return vartype



