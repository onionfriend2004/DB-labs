clean:
	docker-compose down

build:
	docker-compose build

stop:
	docker-compose stop
	
run: stop build
	docker-compose up -d
	python ./lab1/app.py   