#!/usr/bin/env bash

# `test` before publish
bash test.sh || exit 1

# `build` before publish
bash build.sh || exit 1

if [ "$1" = "-t" ] || [ "$1" = "--test" ]; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
else
    twine upload dist/*
fi

