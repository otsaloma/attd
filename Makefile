# -*- coding: utf-8-unix -*-

# EDITOR must wait!
EDITOR = nano

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
	pip3 install --break-system-packages .

# Interactive!
publish:
	$(MAKE) clean
	python3 -m build
	test -s dist/attd-*-py3-none-any.whl
	test -s dist/attd-*.tar.gz
	ls -l dist
	@printf "Press Enter to upload or Ctrl+C to abort: "; read _
	twine upload dist/*
	sudo pip3 uninstall --break-system-packages -y attd || true
	sudo pip3 uninstall --break-system-packages -y attd || true
	sudo pip3 install   --break-system-packages -U attd
	$(MAKE) test-installed

# Interactive!
release:
	$(MAKE) check test clean
	@echo "BUMP VERSION NUMBERS"
	$(EDITOR) attd.py
	@echo "ADD RELEASE NOTES"
	$(EDITOR) NEWS.md
	sudo $(MAKE) install clean
	$(MAKE) test-installed
	tools/release

test:
	py.test .

test-installed:
	cd && python3 -c "import attd; attd.AttributeDict()"

.PHONY: check clean install publish release test test-installed
