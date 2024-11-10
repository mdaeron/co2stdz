def fwcsv(csv, padding = 2):
	csv = [l.split(',') for l in csv.split('\n') if l]
	n = [max([len(l[k]) for l in csv]) for k,_ in enumerate(csv[0])]
	csv = [[e.rjust(n[k] + padding) for k, e in enumerate(l)] for l in csv]
	return '\n'.join([','.join(l) for l in csv])
	
from example_dataset import ds
with open('example_dataset.csv', 'w') as fid:
	fid.write(fwcsv(ds.data.to_csv()))

from example_d13C_setup import ds
with open('example_d13C_data.csv', 'w') as fid:
	fid.write(fwcsv(ds.data.to_csv()))

from example_d13C_standardize import ds
with open('example_d13C_samples.txt', 'w') as fid:
	ds.samples.to_string(fid)
with open('example_d13C_sessions.txt', 'w') as fid:
	ds.sessions['d13C_VPDB'].to_string(fid)

from example_d13C_standardize_force_scaling import ds
with open('example_d13C_force_scaling_samples.txt', 'w') as fid:
	ds.samples.to_string(fid)
with open('example_d13C_force_scaling_sessions.txt', 'w') as fid:
	ds.sessions['d13C_VPDB'].to_string(fid)

from example_d13C_standardize_force_wg import ds
with open('example_d13C_force_wg_samples.txt', 'w') as fid:
	ds.samples.to_string(fid)
with open('example_d13C_force_wg_sessions.txt', 'w') as fid:
	ds.sessions['d13C_VPDB'].to_string(fid)
