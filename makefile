conexion:
	sudo docker network create extractions
	sudo docker volume create db_extractions
compile-local:
	sudo docker-compose -f docker/docker-compose.yml build
	sudo docker-compose -f db/docker-compose.yml build
run-local:
	sudo docker-compose -f docker/docker-compose.yml up -d
	sudo docker-compose -f db/docker-compose.yml up -d
