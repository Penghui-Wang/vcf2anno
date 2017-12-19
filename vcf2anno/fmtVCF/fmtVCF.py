#!/bin/python2.7
# coding:utf-8
import os
from config import vt

def LeftAlign(sts,ref,alt):
    """align the string of ref alt by left and return aligned result"""
    i = 0
    for r,a in zip(ref,alt):
        if r == a:
            i = i + 1
        else:
            break
    ref = ref[i:]
    alt = alt[i:]
    if not ref:
        ref = "-"
    if not alt:
        alt = "-"
    sts = int(sts) + i
    return sts,ref,alt

def RightAlign(sts,ref,alt):
    """align the ref and alt by right and return the result"""
    ref = ref[::-1]
    alt = alt[::-1]
    n = 0
    for r,a in zip(ref,alt):
        if r == a:
            n = n + 1
        else:
            break
    nref = ref[n:]
    nalt = alt[n:]
    if not nref:
        nref = "-"
    if not nalt:
        nalt = "-"
    nref = nref[::-1]
    nalt = nalt[::-1]
    return int(sts),nref,nalt

def formatVar(sts,ref,alt):
    """align the ref and alt by both left and right"""
    sts,ref,alt = LeftAlign(sts,ref,alt)
    sts,ref,alt = RightAlign(sts,ref,alt)
    return str(sts),ref,alt

def breakVcf2(vcf,prefix):
    """seprate the line that cotain more than one alf and
	   and return two line"""
    out = prefix + ".breakmulti.vcf"
    fpw = open(out,"w")

    fp = open(vcf)
    heads = ""
    for line in fp.readlines():
        if line.startswith("#"):
            fpw.write(line)
            continue
        items = line.strip("\n").split("\t")
        chr = items[0]
        sts = items[1]
        ref = items[3]
        alt = items[4]
        alts = alt.split(",")
        for a in alts:
            items[4] = a
            line = "\t".join(items) + "\n"
            fpw.write(line)

    fp.close()

    return out


def breakVcf(vcf,prefix):
    """seprate the line that cotain more than one alf and       and return two line ,use the vt tool """
    out = prefix + ".breakmulti.vcf"
    cmd = "%s decompose %s -o %s" % (vt,vcf,out)
    print cmd
    os.system(cmd)
    return out

def leftAlign(vcf,prefix):
    """align the file by left and right"""
    out = prefix + ".left.vcf"
    fpw = open(out,"w")

    fp = open(vcf)
    heads = ""
    for line in fp.readlines():
        if line.startswith("#"):
            fpw.write(line)
            continue
        items = line.strip("\n").split("\t")
        chr = items[0]
        sts = items[1]
        ref = items[3]
        alt = items[4]
        nsts,nref,nalt = formatVar(sts,ref,alt)      
        items[1]  = nsts
        items[3]  = nref
        items[4]  = nalt
        line = "\t".join(items) + "\n"
        fpw.write(line)
    fp.close()
    return out


def fmtVCF(vcf,prefix):
    """format the input vcf file and return a aligned and
	   breakmultied vcf file"""
    vcf = breakVcf(vcf,prefix)    
    vcf = leftAlign(vcf,prefix)
    return vcf


