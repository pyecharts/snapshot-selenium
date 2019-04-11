all: test

test:
	bash test.sh

format:
	isort -y setup.py $(find snapshot_selenium -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 snapshot_selenium
	black -l 79 setup.py
	black -l 79 tests


lint:
	make lint
