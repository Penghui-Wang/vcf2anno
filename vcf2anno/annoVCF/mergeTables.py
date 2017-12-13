def mergeTables(prefix,file_list):
	files = []
	line = []
	outfile = prefix + ".merged.table"
	fout = open(outfile,'w')
	for fl in file_list:
		files.append(open(fl).readlines())
	for j in range(len(files[0])):
		for i in range(len(files)):
			files[i][j] = files[i][j].strip("\n").split("\t")
		for i in range(len(files)):
			for k in range(5,len(files[i][j])):
				#if files[i][j][k] in files[0][j] and files[i][j][k] not '.':
				#	continue
				#else:
					files[0][j].append(files[i][j][k])
		outline = "\t".join(files[0][j]) + "\n"
		fout.write(outline)
	fout.close()
	return outfile

