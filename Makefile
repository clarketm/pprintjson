.PHONY: format
format:
	python -m black .

.PHONY: build
build: clean
	rm -rf ./dist/*
	python3 setup.py sdist bdist_wheel

.PHONY: test
test:
	python -m nose2 --start-dir . --with-coverage --coverage-report "term" --coverage-report "html"

.PHONY: clean
clean:
	rm -rf ./dist ./build ./*.egg-info ./htmlcov
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: check
check:
	twine check dist/*

.PHONY: upload-test
upload-test: test clean build check
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: upload
upload: test clean build check
	twine upload dist/*

