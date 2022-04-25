network:
	sudo docker network create extractions
volume:
	sudo docker volume create db_extractions
compile-local:
	sudo docker-compose -f docker/docker-compose.yml build && sudo docker-compose -f db/docker-compose.yml build
run-db:
	sudo docker-compose -f db/docker-compose.yml up -d
run-back:
	sudo docker-compose -f docker/docker-compose.yml up -d
