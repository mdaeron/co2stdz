from co2spectroscopy import *

SEED = 9
N = 16
DELTA_SCALING = 0.99
DELTA_OF_WG = -8.

numpy.random.seed(SEED)

sessions = ['2024-10', '2024-11']

samples = {
	'REF_A': -10.0,
	'FOO':    -5.0,
	'REF_B':   0.0,
}

data = [
	{
		'UID': f'A-{k+1:02.0f}',
		'Session': session,
		'Sample': sample,
		'd636': 1000 * (
			(1 + samples[sample] / 1000)
			/ (1 + DELTA_OF_WG / 1000)
			- 1
		) * DELTA_SCALING + numpy.random.normal(scale = 0.05),
	}
	for k, (session, sample) in enumerate(
		zip(
			sessions[:1]*(N//2) + sessions[-1:]*(N - N//2),
			numpy.random.choice(['REF_A', 'REF_B', 'FOO'], size = N),
		)
	)
]

ds = Dataset(data)