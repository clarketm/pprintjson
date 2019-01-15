version=$(shell python -c 'import sys, os; sys.path.insert(0, os.path.abspath(".")); print(__import__("pprintjson").__version__)')

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

.PHONY: tag
tag:
ifeq (,$(shell git tag --list | grep "${version}"))
	git tag "v${version}"
endif

.PHONY: release
release: tag
ifdef version
	curl -XPOST \
	-H "Authorization: token ${GITHUB_ACCESS_TOKEN}" \
	-H "Content-Type: application/json" \
	"https://api.github.com/repos/clarketm/pprintjson/releases" \
	--data "{\"tag_name\": \"v${version}\",\"target_commitish\": \"master\",\"name\": \"v${version}\",\"draft\": false,\"prerelease\": false}"
endif

.PHONY: upload
upload: test clean build check
	twine upload dist/*

