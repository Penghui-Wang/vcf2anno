import os

def test_cns2anno():
	annosv = '/lustre/users/wangpenghui/DevWork/vcf2anno/bin/annosv.py'
	bdfl = '/lustre/users/zhangxu/ProjWork/3.ctDNA/2.call_SV/tog/tog.SV.output'
	prefix = '234'
	cmd = "python %s -i %s -p %s" % (annosv,bdfl,prefix)
	print cmd
	status = os.system(cmd)
	assert status != None

if __name__ =="__main__":
	test_cns2anno()
