#!/usr/bin/env python
#coding:utf-8
__author__ = 'PH.Wang'

def mergeTables(prefix,file_list):
    """merge the annoed tables.

       Args:
       -prefix(str):the output file prefix
       -file_list(list):input files

       Returns:
       -outfile(str):the merged output file
    """
#merge annoed tables,did not take different situation into account
    files = []
    outfile = prefix + ".merged.txt"
    fout = open(outfile,'w')
    for fl in file_list:
        files.append(open(fl).readlines())
    for j in range(len(files[0])):
        for i in range(len(files)):
            files[i][j] = files[i][j].strip("\n").split("\t")
        for i in range(1,len(files)):
            for k in range(5,len(files[i][j])):
                #to make sure matching left colum  
                #if files[i][j][k] in files[0][j]:
                #    if files[i][j][k] is '.':
                #        files[0][j].append(files[i][j][k])
                #    else:
                #        continue
                #else:
                files[0][j].append(files[i][j][k])
        outline = "\t".join(files[0][j]) + "\n"
        fout.write(outline)
    fout.close()
    return outfile

