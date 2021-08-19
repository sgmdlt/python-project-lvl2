repl:
	poetry run ipython

install:
	poetry install

run:
	poetry run gendiff

build:
	rm -rf dist/
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest