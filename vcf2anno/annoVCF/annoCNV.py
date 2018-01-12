#!/usr/lib/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys,os
from config import table_annovar,human_db
import math

def cns2anno(cnsFile, prefix):
    outfile = prefix + '.info.avi.txt'
    fwp = open(outfile, 'w')
    flag = 1
    with open(cnsFile, 'r') as f:
        for line in f:
            if flag == 1:
                flag = 0
                continue
            li = line.split('\t')
            chrom, start, end, log2, cn = li[0],li[1],li[2],li[4],li[5]
            size = int(end)-int(start)+1
            foldchange = str(math.pow(2, float(log2)))
            if int(cn) == 2:
                continue
            if int(cn)>2:
                vartype = 'dup'
            else:
                vartype = 'del'
            fwp.write('\t'.join([chrom, start, end, '0', '0', str(size), vartype, log2, foldchange, cn]))
            fwp.write('\n')
    fwp.close()
    return outfile

    
def annoVCF(aviFile, prefix):
    cmd = "perl %s %s --remove -buildver hg19 %s -protocol refGene,cytoband,dgvMerged,genomicSuperDups,bed  -bed %s -operation g,r,r,r,r -arg ',-colsWanted 4 -minqueryfrac 0.1,-minqueryfrac 0.1,-minqueryfrac 0.1,-colsWanted 4 -minqueryfrac 0.1' -nastring . --outfile %s"%(table_annovar, aviFile, human_db,'hg19_repeatMasker.txt', prefix)
    print(cmd)
    os.system(cmd)
    outFile = prefix + ".hg19_multianno.txt"
    return outFile

def formatAnnoResult(infoFile,annoFile, prefix):
    fp1 = open(infoFile, 'r')
    lines1 = fp1.readlines()
    fp1.close()
    fp2 = open(annoFile, 'r')
    lines2 = fp2.readlines()
    fp2.close()
    outFile = prefix + '.cnv.info.anno.txt'
    fwp = open(outFile, 'w')
    head = ['Chr', 'Start', 'End', 'Size','VarType','Fold_Change(log2)', 'Fold_change','gene_name','gene_region','cytoband','dgvMerged', 'genomicSuperDups', 'repeatMasker']
    fwp.write('\t'.join(head) + '\n')
    for i in range(len(lines1)):
        line1 = lines1[i].strip('\n').split('\t')
        chrom, start, end , size, vartype, log2, foldchange, cn = line1[0], line1[1], line1[2], line1[5],line1[6],line1[7],line1[8],line1[9]
        line2 = lines2[i+1].split('\t')
        gene_name, region, cytoband, dgvMerged, genomicSuperDups, repeat = line2[6], line2[5], line2[10],line2[11],line2[12], line2[13]
        fwp.write('\t'.join([chrom, start, end, size, vartype, log2, foldchange]+[gene_name, region, cytoband, dgvMerged, genomicSuperDups, repeat]))
    fwp.close()


if __name__ == '__main__':
    usage = '''
Usage:
    annoCNV.py -i <cnsinput> -p <prefix>
    annoCNV.py -h | --help
    annoCNV.py -v | --version

Options:
    -h --help                         print usage
    -v --version                      print version information
    -i <cnsinput> --input <cnsinput>  input cnsfile
    -p <prefix> --pref <prefix>       output prefix
'''

    from docopt import docopt
    args = docopt(usage)

    filename = args["--input"]
    prefix = args["--pref"]
    avi = cns2anno(filename, prefix)
    anno = annoVCF(avi, prefix)
    formatAnnoResult(avi, anno, prefix)
