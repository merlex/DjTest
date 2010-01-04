import sys
import os
import os.path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, "/home/httpd/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import django.core.handlers.wsgi

sys.stdout = sys.stderr

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
