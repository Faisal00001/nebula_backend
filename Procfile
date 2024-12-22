web: gunicorn research_lab.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn research_lab.wsgi