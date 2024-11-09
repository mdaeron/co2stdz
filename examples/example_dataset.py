from co2spectroscopy import *

SEED = 2
N = 20

numpy.random.seed(SEED)

samples = {
	'NBS18': (-5.01, -23.01),
	'IAEA603': (2.46, -2.37),
	'FOO': (-13.0, -4.0),
	'BAR': (-3.0, -14.0),
}

data = [
	{
		'UID': f'A-{k+1:02.0f}',
		'Session': session,
		'Sample': sample,
		'd636': numpy.random.normal(scale = 0.05) + samples[sample][0] + 4,
		'd628': numpy.random.normal(scale = 0.05) + samples[sample][1] + 10,
	}
	for k, (session, sample) in enumerate(
		zip(
			['2024-10']*(N//2) + ['2024-11']*(N - N//2),
			numpy.random.choice(list(samples), size = N),
		)
	)
]

ds = Dataset(data)
