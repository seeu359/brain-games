install:
	poetry install
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

brain-even:
	poetry run brain-even

lint:
	poetry run flake8 brain_games

