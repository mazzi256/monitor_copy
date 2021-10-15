env:
	python -m venv env
activate:
	source env/bin/activate
install:
	pip install -r requirements.txt
run-local:
	python manage.py runserver 0.0.0.0:8050
migration:
	python manage.py makemigrations
migrate:
	python manage.py migrate
run:
	docker-compose run web python ./manage.py migrate
	docker-compose build
	docker-compose up
down:
	docker-compose down