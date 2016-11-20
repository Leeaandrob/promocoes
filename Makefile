clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run:clean
	python manage.py runserver 8080

migrate:clean
	python manage.py migrate

migrations:clean
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

shell:clean
	python manage.py shell
