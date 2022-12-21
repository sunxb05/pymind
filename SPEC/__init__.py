"""A typical MOMAP control file momap.inp can be as follows:



.. code-block:: bash


	do_evc                 = 1
	do_spec_tvcf_ft        = 0
	do_spec_tvcf_spec      = 0
	do_ic_tvcf_ft          = 1
	do_ic_tvcf_spec        = 1
	do_isc_tvcf_ft         = 0
	do_isc_tvcf_spec       = 0
	do_spec_sums           = 0	

	&evc 
	...
	/	

	&spec_tvcf
	...
	/	

	&ic_tvcf 
	...
	/	

	&isc_tvcf 
	...
	/	

	&spec_sums
	...
	/


"""
# import logging


# logging.getLogger(__name__).addHandler(logging.NullHandler())

# __author__ = "Xiaobo Sun"
# __email__ = "sunxb05@gmail.com"
# __version__ = "0.1.0"
