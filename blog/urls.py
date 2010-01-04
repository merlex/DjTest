from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('blog.views',
    (r'^$', 'blog_view', {'message': 'urls.py => list blog (EN)'}),
    (r'^(?P<path>.*)/$', 'blogpost_view', {'message': 'urls.py => blog post (EN)'}),
)
