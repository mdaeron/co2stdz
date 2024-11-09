import numpy as np

def pretty_table(x, header = 1, hsep = '  ', vsep = '–', align = '<'):
	'''
	Reads a list of lists of strings and outputs an ascii table

	**Parameters**

	+ `x`: a list of lists of strings
	+ `header`: the number of lines to treat as header lines
	+ `hsep`: the horizontal separator between columns
	+ `vsep`: the character to use as vertical separator
	+ `align`: string of left (`<`) or right (`>`) alignment characters.

	**Example**

	```py
	x = [['A', 'B', 'C'], ['1', '1.9999', 'foo'], ['10', 'x', 'bar']]
	print(pretty_table(x))
	```
	yields:	
	```
	--  ------  ---
	A        B    C
	--  ------  ---
	1   1.9999  foo
	10       x  bar
	--  ------  ---
	```
	
	'''
	txt = []
	widths = [np.max([len(e) for e in c]) for c in zip(*x)]

	if len(widths) > len(align):
		align += '>' * (len(widths)-len(align))
	sepline = hsep.join([vsep*w for w in widths])
	if vsep:
		txt += [sepline]
	for k,l in enumerate(x):
		if k and k == header:
			if vsep:
				txt += [sepline]
		txt += [hsep.join([f'{e:{a}{w}}' for e, w, a in zip(l, widths, align)])]
	if vsep:
		txt += [sepline]
	txt += ['']
	return '\n'.join(txt)

from example_dataset import ds
X = ds.data.to_dict('records')
Y = [[str(_) for _ in X[0]]]
for x in X:
	Y += [[str(x[_])[:8] for _ in x]]
with open('example_dataset.csv', 'w') as fid:
	fid.write(pretty_table(Y, hsep = ',  ', vsep = ''))

from example_d13C_setup import ds
with open('example_d13C_data.txt', 'w') as fid:
	ds.data.to_string(fid)

from example_d13C import ds
with open('example_d13C_samples.txt', 'w') as fid:
	ds.samples.to_string(fid)
with open('example_d13C_sessions.txt', 'w') as fid:
	ds.sessions['d13C_VPDB'].to_string(fid)
