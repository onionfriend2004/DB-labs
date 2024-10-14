clean:
	docker-compose down

build:
	docker-compose build

run: clean build
	docker-compose up -d
	python ./lab1/app.py   