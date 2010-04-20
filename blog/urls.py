from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('blog.views',
	(r'^comments/', include('django.contrib.comments.urls')),
    (r'^$', 'blog_view', {'message': 'urls.py => list blog (EN)'}),
    (r'^tag/(?P<tag>.*)/$', 'blogpost_tag_view', {'message': 'urls.py => blog post (EN)'}),
    (r'^(?P<path>.*)/$', 'blogpost_view', {'message': 'urls.py => blog post (EN)'}),
)
