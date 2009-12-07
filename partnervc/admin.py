from django.contrib import admin
from partnervc.models import CardVC, CategoryVC, HolidayVC, AdditVC
from os.path import join
from djtest import settings


class CardVCAdmin(admin.ModelAdmin):
    list_display  = ('title', 'datepublished')
    list_filter   = ('datepublished',)
    ordering      = ('-datepublished',)
    search_fields = ('title','text')
    
class CategoryVCAdmin(admin.ModelAdmin):
    list_display  = ('nameshort',)
    list_filter   = ('nameshort',)
    ordering      = ('-nameshort',)
    search_fields = ('nameshort','namefull')
    
class HolidayVCAdmin(admin.ModelAdmin):
    list_display  = ('nameshort','month','day',)
    list_filter   = ('day','month')
    ordering      = ('-day','-month',)
    search_fields = ('nameshort','namefull')
    
class AdditVCAdmin(admin.ModelAdmin):
    list_display  = ('key','val',)
    list_filter   = ('key',)
    ordering      = ('-key',)
    search_fields = ('key','val')
    
admin.site.register(CardVC, CardVCAdmin)
admin.site.register(CategoryVC, CategoryVCAdmin)
admin.site.register(HolidayVC, HolidayVCAdmin)
admin.site.register(AdditVC, AdditVCAdmin)
