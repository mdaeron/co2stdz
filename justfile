default: metadata doc

doc:
	cd examples; uv run examples.py
	cd src; uv run ../build_doc.py

test:
	uv run pytest

metadata:
	uv run build-metadata.py

diff:
	git diff --stat -- ':!*.png' ':!*.html' ':!*.pdf' ':!*.csv'

publish:
	uv run flit publish
