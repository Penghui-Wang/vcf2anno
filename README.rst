.. vcf2anno documentation master file, created by
   sphinx-quickstart on Mon Dec 18 09:54:39 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to vcf2anno's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. image:: https://readthedocs.org/projects/vcf2anno/badge/?version=lates
    :target: http://vcf2anno.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

vcf2anno is a quick tool that user the annovar to annotate the vcf files.The main process:

* format the vcf file to normal.
* get the vcf file and abstrate the need information as well as produce an avi file.
* anno the avi file.
* mered the vcf.info and annoed files->merged.table.

this process is very easy and quick.

Introduction
============
This is the introduction of vcf2anno


API
===

.. toctree::
   :maxdepth: 2

   Module Reference <api/modules>

A test of infovcf
=================
This sample infovcf program input a vcf file and get the vcf info that returns a table::

    from infoVCF import InfoVCF
    vcf = "data/mutect.freebayes.breakmulti.vcf"
    prex = "returntest"
    iv = InfoVCF(vcf,prex)
    avi,inv = iv.get_vcf_info()

    print inv

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
