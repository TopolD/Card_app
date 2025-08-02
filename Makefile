ve:
	python3 -m venv .ve; \
	. .ve/bin/activate; \
	pip install -r requirements.txt


lint:
	. .ve/bin/activate; \
	flake8 app
	isort app --diff
	black app --check

