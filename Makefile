repl:
	poetry run ipython

install:
	poetry install

run:
	poetry run gendiff

build: check
	rm -rf dist/
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff/

selfcheck:
	poetry check

check: selfcheck test lint

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build