isort $(find snapshot_selenium -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 snapshot_selenium
black -l 79 tests
