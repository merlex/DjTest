from django.contrib import admin
from blog.models import Blog
from os.path import join
from djtest import settings


class BlogAdmin(admin.ModelAdmin):
    list_display  = ('title', 'publication_date')
    list_filter   = ('publication_date',)
    ordering      = ('-publication_date',)
    search_fields = ('title','body')
    class Media:
	css = {
            'all': ('css/jquery.wysiwyg.css',),
        }
        js = [
            'js/jquery.js',
            'js/ui.core.js',
            'js/ui.dialog.js',
            'js/jquery.wysiwyg.js',
        ]
admin.site.register(Blog, BlogAdmin)
