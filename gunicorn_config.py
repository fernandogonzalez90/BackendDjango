wsgi_app = 'Backend.wsgi:application' 
bind = '0.0.0.0:8000' 
workers = 3
worker_class = 'sync' 