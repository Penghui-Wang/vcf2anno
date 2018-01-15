#!/usr/lib/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys,os
from config import table_annovar,human_db

def lumpyVcf2avi(vcf, prefix):
    outFile = prefix+'.info.avi.txt'
    fwp = open(outFile, 'w')
    with open(vcf, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            li = line.strip('\n').split('\t')
            Chr, Start, End = li[0], li[1], li[1]
            info = li[7].split(';')
            info_dict = {}
            for item in info:
                tmp = item.split('=')
                try:
                    info_dict[tmp[0]] = tmp[1]
                except:
                    pass
            if info_dict['SVTYPE'] in ['DEL', 'DUP']:
                continue
            pos = li[2]
            su = info_dict['SU']
            pe = info_dict['PE']
            sr = info_dict['SR']
            if '_' in pos:
                #gt = li[-1].split(':')[0]
                fwp.write('\t'.join([Chr, Start, End, '0', '0', su, pe, sr]))
                fwp.write('\n')
            else:
                end = info_dict['END']
                fwp.write('\t'.join([Chr, Start, Start, '0', '0', su, pe, sr]))
                fwp.write('\n')
                fwp.write('\t'.join([Chr, end, end, '0', '0', su, pe, sr]))
                fwp.write('\n')
    fwp.close()
    return outFile

def breakdancer2avi(output,prefix):
    outFile = prefix+'.avi.txt'
    fwp = open(outFile, 'w')
    with open(output, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            items = line.strip('\n').split('\t')
            totalreads = items[9]
            Chr1, Start1, End1 = items[0], items[1], items[1]
            Chr2, Start2, End2 = items[3], items[4], items[4]
            aviline = '\t'.join([Chr1,Start1,End1,'0','0',totalreads]) + '\n'
            fwp.write(aviline)
            aviline = '\t'.join([Chr2,Start2,End2,'0','0',totalreads]) + '\n'
            fwp.write(aviline)
            
    fwp.close()
    return outFile 
  
def annoVCF(aviFile, prex):
    cmd = "perl %s %s --remove  -buildver hg19 %s  -protocol refGene -operation g " \
          " -nastring . --outfile %s" % (table_annovar, aviFile, human_db, prex)
    print(cmd)
    os.system(cmd)
    outFile = prex + ".hg19_multianno.txt"
    return outFile

def formatAnnoResult(aviFile,annoFile,prefix):
    head = '\t'.join(['Chr', 'Pos1', 'Gene1', 'Region1', 'Chr2', 'Pos2', 'Gene2', 'Region2','Pair_Reads', 'Split_Reads', 'Total_reads']) + '\n'
    fp = open(aviFile,'r')
    avi = fp.readlines()
    fp.close()
    fa = open(annoFile,'r')
    an = fa.readlines()
    fa.close()
    outFile = prefix + '.mergeavi.anno.txt'
    fout = open(outFile,'w')
    fout.write(head)
    for i in range(0,len(avi),2):
        line1 = avi[i].strip('\n').split('\t')
        line11 = avi[i+1].strip('\n').split('\t')
        chrom1, pos1,total = line1[0],line1[1],line1[5]
        chrom2, pos2 = line11[0], line11[1]
        line2 = an[i+1].strip('\n').split('\t')
        line22 = an[i+2].strip('\n').split('\t')
        gene1, region1 = line2[6],line2[5]
        gene2, region2 = line22[6], line22[5]
        fout.write('\t'.join([chrom1, pos1, gene1, region1, chrom2, pos2, gene2, region2, '-', '-', total]))
        fout.write('\n')
    fout.close()
    return outFile


if __name__ == '__main__':
    usage = '''
Usage:
    annoSV.py -i <brdancerout> -p <prefix> 
    annoSV.py -h | --help
    annoSV.py -v | --version

Options:
    -h --help                       print usage
    -v --version                    print version information
    -i <brdancerout> --input <brdancerout>  input breakdancer out file
    -p <prefix> --pref <prefix>     output prefix
'''

    from docopt import docopt
    args = docopt(usage)
    bdout = args["--input"]
    prefix = args["--pref"]
    avi = breakdancer2avi(bdout, prefix)
    anno = annoVCF(avi, prefix)
    formatAnnoResult(avi,anno, prefix)


