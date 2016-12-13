deps:
	pip install pylint
check: deps
	pylint --rcfile=pylintrc bin/* lib/*
