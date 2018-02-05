#python
import sys
sys.path.append("../")
from vcf2anno.config import table_annovar
from vcf2anno.annoVCF.annoVCF import AnnoVCF

def test_main():
    dbpath = "/lustre/users/yangrui/anno_db/hg19"
    prefix = "multianndb"
    avinput = "data/mutect.avinput"
    test = AnnoVCF(avinput,dbpath,prefix)
    testgenebase = test.gene_based()
    print testgenebase
    testrgbase = test.region_based()
    print testrgbase
    testfilbase = test.filter_based()
    print  testfilbase
    assert (testgenebase,testrgbase,testfilbase) == ("multianndb.Genebased.hg19_multianno.txt","multianndb.Regionbased.hg19_multianno.txt","multianndb.Filterbased.hg19_multianno.txt")
    #testmultidb = test.anno_multidb(db)
    #print testmultidb


if __name__ == "__main__":
    pytest.main()
