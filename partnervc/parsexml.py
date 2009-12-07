#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
import psycopg2

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

try:
    conn = psycopg2.connect("dbname='djtest' user='djtest' host='localhost' password='djtest' port='5433'");
except:
    print "I am unable to connect to the database"
    
cur = conn.cursor()
cur.execute("""SELECT * FROM partnervc_additvc""")
rows = cur.fetchall()
print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]
    pprint(row)

src = './voicecards.xml'
tree = etree.parse(src)
#r = tree.xpath('/voicecards/cards/card')

r = tree.xpath('/voicecards/additional')
print(len(r))
i = 0
for element in tree.xpath("/voicecards/cards/card"):
    s = ''
    i += 1
    for child in element.iterchildren():
        s += ("%s - %s\r\n" % (child.tag, child.text))
    print(s+"\r\n")
print('i='+str(i))
#for rval in r:
#    pprint(rval[1].tag.encode("utf-8"))
#    pprint(rval[1].text.encode("utf-8"))
    #cur.execute("""INSERT INTO partnervc_additvc("key", val)    VALUES (?, ?, ?);""")
#    for child in rval.iterchildren():
#        if(child.tag == 'title'):
#            print(child.text)
#        print(child.tag)
