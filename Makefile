all: deps check test image

## Static Analysis ##
deps:
	pip install pylint
check: deps
	pylint --rcfile=pylintrc bin/* lib/*

## Pre-Deployment Testing ##
test:
	make -C test

## Docker Image Build ##
image:
	docker build --pull -t yinc2/fibonacci-web-service:latest -f Dockerfile .

clean:
	rm -f bin/*.pyc lib/*.pyc test/*.pyc

.PHONY: test clean
