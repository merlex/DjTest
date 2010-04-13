# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import datetime
from blog.models import Blog
from tagging.models import Tag, TaggedItem
from pprint import pprint

def blog_view(request, **kw):
    blog_list = Blog.objects.order_by('-publication_date')
    now = datetime.datetime.now()
    kw['now'] = now
    kw['blog_list'] = blog_list
    context = RequestContext(request, kw)
    return render_to_response("blog/blog_list.html", context)

def blogpost_view(request, **kw):
    blog = Blog.objects.get(slug = kw['path'])
    pprint(blog)
    kw['blog'] = blog
    context = RequestContext(request, kw)
    return render_to_response("blog/blog_post.html", context)
def blogpost_tag_view(request, **kw):
    query_tag = Tag.objects.get(name=kw['tag'])
    blog_list = TaggedItem.objects.get_by_model(Blog, query_tag)
    kw['blog_list'] = blog_list
    context = RequestContext(request, kw)
    return render_to_response("blog/blog_list.html", context)
