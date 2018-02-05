import os
import sys
sys.path.append('..')
def test_cns2anno():
    cns2anno = '../bin/cns2anno.py'
    cns = 'data/RD013-AgE02.call.cns'
    prefix = '123'
    cmd = "python %s -i %s -p %s" % (cns2anno,cns,prefix)
    print cmd
    status = os.system(cmd)
    assert status != None

if __name__ =="__main__":
    test_cns2anno()
