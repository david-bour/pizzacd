docker-run:
	docker-compose -f docker-compose.yml -f docker-compose.middleware.yml up -d

docker-all:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.middleware.yml up -d

docker-build-all: docker-stop
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.middleware.yml up --build -d

docker-debug:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.middleware.yml -f docker-compose.debug.yml up -d

docker-stop:
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm

docker-clean: docker-stop
	docker system prune -a

pizzas:
	for i in {1..50}; do \
		http POST http://localhost/api/graph/pepperoni ; \
	done

pizzas-dev:
	for i in {1..50}; do \
		http POST http://localhost:5000/graph/pepperoni ; \
	done

