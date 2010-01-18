 # -*- coding: utf-8 -*-
# Create your views here.
from djtest.partnervc.models import HolidayVC
from djtest.partnervc.models import CategoryVC
from djtest.partnervc.models import CardVC
from django.shortcuts import render_to_response
from django.template.context import RequestContext
#from django.db.models import DoesNotExist
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
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_cards(request, **kw):
    addit = []
    CardVC.objects.all().delete()
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
        hol = HolidayVC(id = int(card['holidayid']))
        cat = CategoryVC(id = int(card['catid']))
        cards = CardVC(id = int(card['cardid']),
                       title = card['title'],
                       path = card['path'],
                       catid = cat,
                       holidayid = hol,
                       text = card['text'],
                       playtime = int(card['playtime']),
                       numorders_24 = int(card['numorders_24']),
                       numorders_7 = int(card['numorders_7']),
                       numorders_30 = int(card['numorders_30']),
                       datepublished = time.strftime('%Y-%m-%d',time.strptime(card['datepublished'], '%Y-%m-%d %H:%M:%S')))
        cards.save()
    kw['count'] = c
    kw['addit'] = addit
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_category(request, **kw):
    addit = []
    CategoryVC.objects.all().delete()
    CategoryVC(id = 0,
               parentid = 0,
               nameshort = '0',
               namefull = '0',
               catpath = '0',
               ispublished = 0).save()
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
        catg = CategoryVC(id = int(cat['catid']),
                          parentid = int(cat['parentid']),
                          nameshort = cat['nameshort'],
                          namefull = cat['namefull'],
                          catpath = cat['catpath'],
                          ispublished = int(cat['ispublished']))
        catg.save()
    kw['count'] = c
    kw['addit'] = addit
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def export_holidays(request, **kw):
    addit = []
    HolidayVC.objects.all().delete()
    HolidayVC(id = 0,
              nameshort = '0',
              namefull = '0',
              month = 0,
              day = 0,
              icon = '0').save()
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
        hols = HolidayVC(id = int(hol['holid']),
                         nameshort = hol['nameshort'],
                         namefull = hol['namefull'],
                         month = int(hol['month']),
                         day = int(hol['day']),
                         icon = hol['icon'])
        hols.save()
    kw['count'] = c
    kw['addit'] = addit
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)

def main_page_view(request, **kw):
    months = [ u'', u'января', u'февраля', u'марта',
                    u'апреля', u'мая', u'июня', u'июля',
                    u'августа', u'сентября', u'октября', u'ноября', u'декабря']
    curdate = time.localtime(time.time())

    categories = CategoryVC.objects.filter(ispublished=1).order_by('parentid')
    catgs = {}
    catgs2 = []
    for cat in categories:
        if cat.parentid == 0:
            catgs[cat.id] = {'id': cat.id, 'name':cat.nameshort, 'childs':[]}
        else:
            catgs[cat.parentid]['childs'].append({'id': cat.id, 'name':cat.nameshort})
    for cat in catgs:
        catgs2.append(catgs[cat])

    hols = []
    counter = 0
    for i in range(10):
        if len(hols) > 5:
            break
        holidays = HolidayVC.objects.extra(where=['(month=%s AND day>=%s) OR (month>%s AND day>0)'],
                                           params=[curdate.tm_mon,curdate.tm_mday,curdate.tm_mon]).order_by('month','day')[i*6:(i+1)*6]
        for hol in holidays:
            c = 0
            if counter%3 == 0:
                c = 1
            today = 0
            if hol.day == curdate.tm_mday and hol.month == curdate.tm_mon:
                today = 1
            cards = CardVC.objects.filter(holidayid = hol.id).count()
            if not cards or len(hols) > 5:
                continue
            hols.append({'id': hol.id, 'name':hol.nameshort, 'img':hol.icon,
                         'day':hol.day, 'month':months[hol.month],
                         'today':today, 'counter':c,'cards':cards})
            counter += 1

    cards = getCardList()
    bcards = getCardList(80399)
    jcards = getCardList(80422)
    kw['categories'] = catgs2
    kw['holidays']   = hols
    kw['cards']      = cards
    kw['bcards']     = bcards
    kw['jcards']     = jcards
#    pprint(holidays)
    context = RequestContext(request, kw)
    return render_to_response("partnervc/main_page.html", context)

def getCardList(catg=0, sortfield='-numorders_30',count=18):
    """Documentation"""
    if catg:
        catgs = ''
        for cat in CategoryVC.objects.extra(where=['id = %s OR parentid = %s' % (catg, catg)]):
            catgs +=  ','+str(cat.id)
        cards = CardVC.objects.extra(where=[' catid_id IN(0'+catgs+')']).order_by(sortfield)[:count]
    else:
        cards = CardVC.objects.order_by(sortfield)[:count]
    cards2 = []
    counter = 0
    for card in cards:
        c = 0
        c2 = 0
        if counter%6 == 0:
            c = 1
        if counter%3 == 0:
            c2 = 1
        cards2.append({'id': card.id, 'name':card.title, 'catid':card.catid,
                       'counter':c,'counter2':c2})
        counter += 1
    return cards2
