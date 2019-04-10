pip freeze
nosetests --with-coverage --cover-package snapshot_selenium --cover-package tests tests snapshot_selenium && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
