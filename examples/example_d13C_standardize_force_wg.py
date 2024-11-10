from co2spectroscopy import *

ds = Dataset()
ds.read_csv('example_d13C_data.csv')

anchors = {
	'REF_B': 0.0,
}

sessions = set(ds.data.Session)

ds.standardize(
	k_in = 'd636',
	k_out = 'd13C_VPDB',
	anchors = anchors,
	constraints = {'delta_of_wg_' + sanitize(s): '-8.0' for s in sessions},
)