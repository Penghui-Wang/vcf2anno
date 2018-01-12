import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoCNS import InfoCNS

def test_incns():
	cns = "/lustre/users/zhangxu/ProjWork/3.ctDNA/1.call_CNV/RD001-AgA01.call.cns"
	prex = "cns"
	ic = InfoCNS(cns,prex)
	avi,inc = ic.get_cns_info()
	assert avi,inc ==("cns.avinput","cns.cns.info")

if __name__ == "__main__":
	pytest.test_incns()
