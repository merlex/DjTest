from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('accounts.views',
    (r'^login/', 'login', {'message': 'urls.py => login'}),
	(r'^logout/', 'logout', {'message': 'urls.py => logout'}),
    (r'^loggedin/', 'loggedin', {'message': 'urls.py => loggedin'}),
    (r'^invalid/', 'invalid', {'message': 'urls.py => invalid'}),
)
