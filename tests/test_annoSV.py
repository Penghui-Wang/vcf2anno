import os
import sys
sys.path.append("../")

def test_cns2anno():
	annosv = '../bin/annosv.py'
	bdfl = 'data/tog.SV.output'
	prefix = '234'
	cmd = "python %s -i %s -p %s" % (annosv,bdfl,prefix)
	print cmd
	status = os.system(cmd)
	assert status != None

if __name__ =="__main__":
	test_cns2anno()
