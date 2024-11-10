from co2spectroscopy import *

ds = Dataset()
ds.read_csv('example_d13C_data.csv')

anchors = {
	'REF_A': -10.0,
	'REF_B':   0.0,
}

ds.standardize(k_in = 'd636', k_out = 'd13C_VPDB', anchors = anchors)
