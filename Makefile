.PHONY: all clean test

all: test clean dist

clean:
	rm -rf .coverage .pytest_cache/ NothingDoer.egg-info/ build/ dist/ results.xml
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

test:
	docker run --rm -t -v `pwd`:/work -w /work themattrix/tox

dist:
	python setup.py sdist
