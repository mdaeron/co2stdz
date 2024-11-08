from co2spectroscopy import *
from pytest import approx

def test_estimate_covariance():
	CM = estimate_covariance(
		numpy.array([
			[1.0,1.0],
			[0.0,0.0],
			[0.1,0.0],
			[1.0,1.1],
			[0.5,0.5],
		]), robust = False,
	)
	assert CM[0,0] == approx(0.227)
	assert CM[0,1] == approx(0.2495)
	assert CM[1,0] == approx(0.2495)
	assert CM[1,1] == approx(0.277)

def test_standardize():
	ds = Dataset([
		{'Session': 'foo', 'Sample': 'REF_A',   'd636': -0.01},
		{'Session': 'foo', 'Sample': 'REF_A',   'd636':  0.01},
		{'Session': 'foo', 'Sample': 'BAR', 'd636':  5.0},
		{'Session': 'foo', 'Sample': 'REF_B',   'd636':  9.99},
		{'Session': 'foo', 'Sample': 'REF_B',   'd636': 10.01},
	])
	ds.standardize(
		k_in = 'd636',
		k_out = 'd13C_VPDB',
		anchors = {
			'REF_A': 0.0,
			'REF_B': 10.0,
		},
	)
	assert ds.samples.loc['BAR']['d13C_VPDB'] == approx(5.0)
	assert ds.sessions['d13C_VPDB'].loc['foo']['d636_scaling'] == approx(1, 1e-5)
	assert ds.sessions['d13C_VPDB'].loc['foo']['d13C_VPDB_of_wg'] == approx(0, 0, 3e-5)
