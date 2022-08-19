build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

brain-games:
	poetry run brain-games