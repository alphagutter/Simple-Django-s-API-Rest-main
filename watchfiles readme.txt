para activar el entorno virtual:

	venv\Scripts\activate

para alzar mi proyecto:

	python manage.py runserver

conectar a redis desde docker:
	
	docker exec -it redis redis-cli

conectar el celery (sin watchfiles):

python -m celery -A django_celery worker

python -m celery -A django_celery worker -l info

el celery no funciona sin gevent, así que lo instalamos, modificamos el código y funciona
linea para conectar el celery con gevent:
	celery -A django_celery worker -P gevent --loglevel=INFO


para correr el celery con el watchfiles es así:

	watchfiles --filter python 'celery -A django_celery_example worker --loglevel=info'

!el watchfiles sirve para resetear automaticamente nuestro celery cuando modificamos nuestro codigo

	+así queda nuestro watchfiles para este proyecto en concreto
	watchfiles --filter python 'celery -A django_celery worker --loglevel=info'
	
	watchfiles --target-type command --filter python 'celery -A django_celery worker --loglevel=info'
