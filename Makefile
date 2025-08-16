ve:
	python3 -m venv .ve; \
	. .ve/bin/activate; \
	pip install -r requirements.txt


docker_build_mongodb:
	docker run -d --name mongo \
	mongo

docker_build:
	docker-compose up -d --build

docker_down:
	docker-compose down

tests:
	export MODE=test && python -m pytest -v


lint:
	flake8 conduit
	isort conduit --diff
	black conduit --check
	mypy --namespace-packages -p "conduit" --config-file setup.cfg
