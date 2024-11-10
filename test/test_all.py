from co2stdz import *
from pytest import approx

def test_estimate_covariance():
	XY = numpy.array([
		[1.0,1.0],
		[0.0,0.0],
		[0.1,0.0],
		[1.0,1.1],
		[0.5,0.5],
	])
	CM = estimate_covariance(XY, robust = False)
	assert CM[0,0] == approx(0.227)
	assert CM[0,1] == approx(0.2495)
	assert CM[1,0] == approx(0.2495)
	assert CM[1,1] == approx(0.277)

	CM = estimate_covariance(XY, robust = True)
	assert CM[0,0] == approx(0.452)
	assert CM[0,1] == approx(0.47)
	assert CM[1,0] == approx(0.47)
	assert CM[1,1] == approx(0.492)


def test_cov_ellipse():
	width, height, rotation = cov_ellipse([[1.0, 0.5], [0.5, 1.0]])
	assert width == approx(3.46163677)
	assert height == approx(5.99573075)
	assert rotation == approx(135)


def test_standardize():
	ds = Dataset([
		{'Session': 'foo', 'Sample': 'REF_A', 'd636': -0.01},
		{'Session': 'foo', 'Sample': 'REF_A', 'd636':  0.01},
		{'Session': 'foo', 'Sample': 'BAR',   'd636':  5.00},
		{'Session': 'foo', 'Sample': 'REF_B', 'd636':  9.99},
		{'Session': 'foo', 'Sample': 'REF_B', 'd636': 10.01},
	])

	anchors = {
		'REF_A': 0.0,
		'REF_B': 10.0,
	}

	for method in [
		'correct_observations',
		'predict_observations',
	]:
		ds.standardize(
			k_in = 'd636',
			k_out = 'd13C_VPDB',
			anchors = anchors,
			method = method,
		)
		assert numpy.round(ds.samples.loc['BAR']['d13C_VPDB'], 3) == 5.
		assert numpy.round(ds.sessions['d13C_VPDB'].loc['foo']['d636_scaling'], 4) == 1.
		assert numpy.round(ds.sessions['d13C_VPDB'].loc['foo']['d13C_VPDB_of_wg'], 3) == 0.


def test_standardize_D17O():
	ds = Dataset([
		{'Session': 'foo', 'Sample': 'REF_A', 'd628': -0.01, 'd627': -0.01},
		{'Session': 'foo', 'Sample': 'REF_A', 'd628':  0.01, 'd627':  0.01},
		{'Session': 'foo', 'Sample': 'BAR',   'd628':  4.99, 'd627':  2.51},
		{'Session': 'foo', 'Sample': 'BAR',   'd628':  5.01, 'd627':  2.49},
		{'Session': 'foo', 'Sample': 'REF_B', 'd628':  9.99, 'd627':  4.99},
		{'Session': 'foo', 'Sample': 'REF_B', 'd628': 10.01, 'd627':  5.01},
	])

	anchors = {
		'REF_A': {'d18O_VSMOW':  0.0, 'D17O_VSMOW': 0.0, },
		'REF_B': {'d18O_VSMOW': 10.0, 'D17O_VSMOW': 0.0, },
	}

	for method in [
		'correct_observations',
		'predict_observations',
	]:
		for residuals_17 in [
			'D17',
			'd17',
		]:
			ds.standardize_D17O(
				d18O_key_in = 'd628',
				d17O_key_in = 'd627',
				d18O_key_out = 'd18O_VSMOW',
				d17O_key_out = 'd17O_VSMOW',
				anchors = anchors,
				method = method,
				residuals_17 = residuals_17,
			)
			assert numpy.round(ds.samples.loc['BAR']['d18O_VSMOW'], 3) == 5.
			assert numpy.round(ds.samples.loc['BAR']['D17O_VSMOW'], 4) == -0.0031
			assert numpy.round(ds.sessions['D17O_VSMOW'].loc['foo']['d628_scaling'], 3) == 1.
			assert numpy.round(ds.sessions['D17O_VSMOW'].loc['foo']['d627_scaling'], 3) == 0.949
			assert numpy.round(ds.sessions['D17O_VSMOW'].loc['foo']['d18O_VSMOW_of_wg'], 3) == 0.
			assert numpy.round(ds.sessions['D17O_VSMOW'].loc['foo']['d17O_VSMOW_of_wg'], 3) == 0.
	
			del ds.sessions
			del ds.samples


def test_standardize_water_eq_CO2_D17O():
	ds = Dataset([
		{'Session': 'foo', 'Sample': 'REF_A', 'd628': -0.01, 'd627': -0.01},
		{'Session': 'foo', 'Sample': 'REF_A', 'd628':  0.01, 'd627':  0.01},
		{'Session': 'foo', 'Sample': 'BAR',   'd628':  4.99, 'd627':  2.51},
		{'Session': 'foo', 'Sample': 'BAR',   'd628':  5.01, 'd627':  2.49},
		{'Session': 'foo', 'Sample': 'REF_B', 'd628':  9.99, 'd627':  4.99},
		{'Session': 'foo', 'Sample': 'REF_B', 'd628': 10.01, 'd627':  5.01},
	])
	ds.data['H2O/CO2'] = 200.
	ds.data['eqCO2_d18O_VSMOW'] = 10.
	ds.data['eqCO2_D17O_VSMOW'] = -0.15
	ds.data['eqCO2_d13C_VPDB'] = -5.
	

	anchors = {
		'REF_A': {'d18O_VSMOW':  0.0, 'D17O_VSMOW': 0.0, },
		'REF_B': {'d18O_VSMOW': 10.0, 'D17O_VSMOW': 0.0, },
	}

	for method in [
		'correct_observations',
		'predict_observations',
	]:
		for residuals_17 in [
			'D17',
			'd17',
		]:
			ds.standardize_water_eq_CO2_D17O(
				d18O_key_in = 'd628',
				d17O_key_in = 'd627',
				d18O_key_out = 'd18O_VSMOW',
				d17O_key_out = 'd17O_VSMOW',
				water_anchors = anchors,
				method = method,
				residuals_17 = residuals_17,
				alpha18_CO2g_H2O = 1.041036, # Barkan & Luz (2012)
				theta17_CO2g_H2O = 0.5229,   # Barkan & Luz (2012)
				R13_VPDB = 0.01118,
				R18_VSMOW = 0.00200520,
				R17_VSMOW = 0.00038475,
				lambda_17 = 0.528,
			)
			assert numpy.round(ds.samples.loc['BAR']['water_d18O_VSMOW'], 3) == 5.
			assert numpy.round(ds.samples.loc['BAR']['water_D17O_VSMOW'], 4) == -0.0031
			assert numpy.round(ds.sessions['water_D17O_VSMOW'].loc['foo']['d628_scaling'], 3) == 1.010
			assert numpy.round(ds.sessions['water_D17O_VSMOW'].loc['foo']['d627_scaling'], 3) == 0.959
			assert numpy.round(ds.sessions['water_D17O_VSMOW'].loc['foo']['d18O_VSMOW_of_wg'], 3) == 40.716
			assert numpy.round(ds.sessions['water_D17O_VSMOW'].loc['foo']['d17O_VSMOW_of_wg'], 3) == 21.089
	
			del ds.sessions
			del ds.samples
