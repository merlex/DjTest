from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('partnervc.views',
    (r'^export/$', 'export_view', {'message': 'urls.py => export (EN)'}),
)
