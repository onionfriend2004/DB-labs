clean:
	docker-compose down

build:
	docker-compose build

stop:
	docker-compose stop
	
run: stop build
	docker-compose up -d
	python3 ./lab1/app.py   