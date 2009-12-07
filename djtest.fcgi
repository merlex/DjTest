#!/usr/bin/python
import fastcgi

import os, sys
sys.path.append('/home/httpd')
sys.path.append('/home/httpd/djtest')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djtest.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
s = fastcgi.ThreadedWSGIServer(application, workers=5)
s.serve_forever()
