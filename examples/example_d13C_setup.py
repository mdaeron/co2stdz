from co2spectroscopy import *

SEED = 13
N = 16

numpy.random.seed(SEED)

sessions = ['2024-10', '2024-11']

anchors = {
	'REF_A': 0.0,
	'REF_B': 10.0,
}

data = [
	{
		'UID': f'A-{k+1:02.0f}',
		'Session': session,
		'Sample': sample,
		'd636': numpy.random.normal(scale = 0.05) + (anchors[sample] if sample in anchors else 5.0),
	}
	for k, (session, sample) in enumerate(
		zip(
			sessions[:1]*(N//2) + sessions[-1:]*(N - N//2),
			numpy.random.choice(['REF_A', 'REF_B', 'FOO'], size = N),
		)
	)
]

ds = Dataset(data)
