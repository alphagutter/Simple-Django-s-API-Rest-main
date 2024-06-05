# venv/run_celery.py

import subprocess

subprocess.call(['python', '-m', 'celery', '-A', 'django_celery', 'worker', '--loglevel=info'])
