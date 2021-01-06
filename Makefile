.PHONY: clean build install test
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	python3 setup.py clean
build:
	python3 setup.py build
install: build
	python3 setup.py install
test: build
	python3 test.py
push: test
	git push origin master

