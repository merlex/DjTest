from django.db import models
from django.contrib import admin
from datetime import datetime, date
from django.utils.translation import ugettext_lazy as _
from os.path import join
from djtest import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(_("slug"), max_length=255, db_index=True, unique=False)
    body = models.TextField(_("body"))
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

#admin.site.register(Blog)
