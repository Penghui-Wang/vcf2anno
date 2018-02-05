import sys
sys.path.append("../")
from vcf2anno.infoVCF.infoCNS import InfoCNS

def test_incns():
    cns = "data/RD001-AgA01.call.cns"
    prex = "21"
    ic = InfoCNS(cns,prex)
    avi,inc = ic.get_cns_info()
    assert avi,inc ==("cns.avinput","cns.cns.info")

if __name__ == "__main__":
    pytest.test_incns()
