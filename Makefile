# -*- coding: utf-8-unix -*-

PREFIX = /usr/local

check:
	flake8 .

clean:
	rm -rf attd.egg-info
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf .pytest_cache
	rm -rf */.pytest_cache

install:
	./setup.py install --prefix=$(PREFIX)

test:
	py.test .

.PHONY: check clean install test
