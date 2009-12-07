# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from partnervc.models import AdditVC
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
    src = '/home/httpd/djtest/partnervc/voicecards.xml'
    tree = etree.parse(src)
    r = tree.xpath('/voicecards/additional')
    c = 0
#    for element in tree.xpath("//additional/*"):
#        c +=1
#        a = AdditVC(key=element.tag,val=element.text)
#        a.save()
    kw['count'] = c
    context = RequestContext(request, kw)
    return render_to_response("partnervc/export_status.html", context)
