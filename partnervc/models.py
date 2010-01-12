from django.db import models
from datetime import datetime, date
from django.utils.translation import ugettext_lazy as _
from calendar import month
from os.path import join
from djtest import settings

# Create your models here.
class CategoryVC(models.Model):
    """
    Model Category
    """
    parentid = models.IntegerField()
    nameshort = models.CharField(max_length=255)
    namefull = models.TextField(_("text"))
    catpath = models.CharField(max_length=255)
    ispublished = models.IntegerField()

    def __unicode__(self):
        return self.nameshort

class HolidayVC(models.Model):
    """
    Model Holiday
    """
    nameshort = models.CharField(max_length=255)
    namefull = models.TextField(_("text"))
    month = models.IntegerField()
    day = models.IntegerField()
    icon = models.URLField()

    def __unicode__(self):
        return '%s %s-%s' % (self.nameshort,self.day,self.month)

class CardVC(models.Model):
    """
    Model Card
    """
    title = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    catid = models.ForeignKey(CategoryVC)
    holidayid = models.ForeignKey(HolidayVC)
    text = models.TextField(_("text"))
    playtime = models.IntegerField()
    numorders_24 = models.IntegerField()
    numorders_7 = models.IntegerField()
    numorders_30 = models.IntegerField()
    datepublished = models.DateField()

    def __unicode__(self):
        return self.title

class AdditVC(models.Model):
    """
    Model additional params
    """
    key = models.CharField(max_length=255)
    val = models.CharField(max_length=255)

    def __unicode__(self):
        return self.key

