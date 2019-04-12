all: test

test:
	bash test.sh

format:
	isort -rc .
	black -l 79 snapshot_selenium
	black -l 79 setup.py
	black -l 79 tests


lint:
	make lint
