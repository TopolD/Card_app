ve:
	python3 -m venv .ve; \
	. .ve/bin/activate; \
	pip install -r requirements.txt




docker_build:
	docker-compose up -d --build

docker_down:
	docker-compose down

tests:
	export MODE=test && python -m pytest -v


lint:
	flake8 app
	isort app --diff
	black app --check
