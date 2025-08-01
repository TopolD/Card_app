

test:
	export MODE=TEST python -m pytest -v ./app/tests

lint:
	flake8 conduit
	isort conduit --diff
	black conduit --check
	mypy --namespace-packages -p "conduit" --config-file setup.cfg



docker_build:
	docker-compose up -d --build

docker_build_mongo:
	docker-compose up -d mongo --build

docker_up:
	docker-compose up -d

docker_down:
	docker-compose down
