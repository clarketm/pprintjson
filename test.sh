#!/usr/bin/env sh

python -m nose2 --start-dir . --with-coverage --coverage-report "term" --coverage-report "html" $@
