# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import datetime
from blog.models import Blog

def blog_view(request, **kw):
    blog_list = Blog.objects.all()
    now = datetime.datetime.now()
    kw['now'] = now
    kw['blog_list'] = blog_list
    context = RequestContext(request, kw)
    return render_to_response("blog/blog_list.html", context)
