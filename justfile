doc:
	cd examples; uv run examples.py
	cd src; uv run ../build_doc.py

test:
	uv run pytest

metadata:
	uv run build-metadata.py
