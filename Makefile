install:
	poetry install
	poetry publish --dry-run
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

lint:
	poetry run flake8 brain_games
