pip freeze
nosetests --with-coverage --cover-package snapshot_selenium --cover-package tests tests  docs/source snapshot_selenium && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
