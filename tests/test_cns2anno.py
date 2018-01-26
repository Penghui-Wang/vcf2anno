import os

def test_cns2anno():
	cns2anno = '/lustre/users/wangpenghui/DevWork/vcf2anno/bin/cns2anno.py'
	cns = '/lustre/users/zhangxu/ProjWork/3.ctDNA/1.call_CNV/RD013-AgE02.call.cns'
	prefix = '123'
	cmd = "python %s -i %s -p %s" % (cns2anno,cns,prefix)
	print cmd
	status = os.system(cmd)
	assert status != None

if __name__ =="__main__":
	test_cns2anno()
