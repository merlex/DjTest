from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('partnervc.views',
    (r'^$', 'main_page_view', {'message': 'urls.py => main page view'}),
    (r'^export/$', 'export_view', {'message': 'urls.py => export test'}),
    (r'^export/addit/$', 'export_addit', {'message': 'urls.py => export additionals'}),
    (r'^export/cards/$', 'export_cards', {'message': 'urls.py => export cards'}),
    (r'^export/category/$', 'export_category', {'message': 'urls.py => export category'}),
    (r'^export/holidays/$', 'export_holidays', {'message': 'urls.py => export holidays'}),
    (r'^export/card2cat/$', 'export_card2cat', {'message': 'urls.py => export cards'}),
)
