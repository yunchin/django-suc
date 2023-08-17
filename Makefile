all:
	python3 -m build

test:
	pytest tests

clean:
	rm -rf build dist *.egg-info .tox
