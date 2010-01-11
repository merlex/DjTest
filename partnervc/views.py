# Create your views here.
from djtest.partnervc.models import HolidayVC
from djtest.partnervc.models import CategoryVC
from djtest.partnervc.models import CardVC
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from partnervc.models import AdditVC
from pprint import pprint
import time
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

def export_view(request, **kw):
    addit = []
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
    #for element in tree.xpath("//additional/*"):
    for element in tree.xpath("/voicecards/cards/card"):
        card = {}
        for child in element.iterchildren():
            card[child.tag] = child.text
#            addit.append({'text':element.text, 'tag':element.tag, 'c':c})
        c +=1
        addit.append(card)
    kw['count'] = c
    kw['addit'] = addit
    pprint(addit)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_addit(request, **kw):
    addit = []
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
    for element in tree.xpath("//additional/*"):
        addit.append({'text':element.text, 'tag':element.tag, 'c':c})
        c +=1
        a = AdditVC(key=element.tag,val=element.text)
        a.save()
    kw['count'] = c
    kw['addit'] = addit
    pprint(addit)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_cards(request, **kw):
    addit = []
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
    for element in tree.xpath("/voicecards/cards/card"):
        card = {}
        for child in element.iterchildren():
            card[child.tag] = child.text
        c +=1
        addit.append(card)
        if not card['text']:
            card['text'] = ''
        cards = CardVC(title = card['title'],
                       cardid = int(card['cardid']),
                       path = card['path'],
                       catid = int(card['catid']),
                       holidayid = int(card['holidayid']),
                       text = card['text'],
                       playtime = int(card['playtime']),
                       numorders_24 = int(card['numorders_24']),
                       numorders_7 = int(card['numorders_7']),
                       numorders_30 = int(card['numorders_30']),
                       datepublished = time.strftime('%Y-%m-%d',time.strptime(card['datepublished'], '%Y-%m-%d %H:%M:%S')))
        cards.save()
    kw['count'] = c
    kw['addit'] = addit
    pprint(addit)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_category(request, **kw):
    addit = []
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
    for element in tree.xpath("/voicecards/categories/category"):
        cat = {}
        for child in element.iterchildren():
            cat[child.tag] = child.text
        c +=1
        addit.append(cat)
        catg = CategoryVC(catid = int(cat['catid']),
                          parentid = int(cat['parentid']),
                          nameshort = cat['nameshort'],
                          namefull = cat['namefull'],
                          catpath = cat['catpath'],
                          ispublished = int(cat['ispublished']))
        catg.save()
    kw['count'] = c
    kw['addit'] = addit
    pprint(addit)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_holidays(request, **kw):
    addit = []
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
    for element in tree.xpath("/voicecards/holidays/holiday"):
        hol = {}
        for child in element.iterchildren():
            hol[child.tag] = child.text
        c +=1
        addit.append(hol)
        hols = HolidayVC(holid = int(hol['holid']),
                         nameshort = hol['nameshort'],
                         namefull = hol['namefull'],
                         month = int(hol['month']),
                         day = int(hol['day']),
                         icon = hol['icon'])
        hols.save()
    kw['count'] = c
    kw['addit'] = addit
    pprint(addit)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def main_page_view(request, **kw):
    categories = CategoryVC.objects.order_by('parentid')
    catgs = {}
    catgs2 = []
    for cat in categories:
        if cat.parentid == 0:
            catgs[cat.catid] = {'id': cat.catid, 'name':cat.nameshort, 'childs':[]}
        else:
            catgs[cat.parentid]['childs'].append({'id': cat.catid, 'name':cat.nameshort})
    for cat in catgs:
        catgs2.append(catgs[cat])
    kw['categories'] = catgs2
    pprint(catgs2)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/main_page.html", context)
