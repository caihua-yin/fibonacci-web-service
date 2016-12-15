SERVICE_NAME ?= store-service
DOCKER_TAG ?= latest

all: deps check test image

## Static Analysis ##
deps:
	pip install pylint
check: deps
	pylint --rcfile=pylintrc bin/* lib/*

## Pre-Deployment Testing ##
test: check
	make -C test

## Docker Image Build ##
image: test
	docker build --pull -t yinc2/$(SERVICE_NAME):$(DOCKER_TAG) -f Dockerfile .

## Docker Image Push ##
push: image
	docker push yinc2/$(SERVICE_NAME):$(DOCKER_TAG)

clean:
	rm -f bin/*.pyc lib/*.pyc test/*.pyc

.PHONY: test clean
