# -*- coding: iso-8859-1, utf-8 -*-
# Created on 01.11.2015 by @author: PeterH 

import urllib
import xml.etree.ElementTree as ET

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_189084.xml'
uh = urllib.urlopen(url).read()
tree = ET.fromstring(uh)
numberofcomments = tree.findall('.//comment')
totalcount = 0
for count in numberofcomments:
    numbercount = count.find('count').text
    totalcount = totalcount + int(numbercount)
print len(numberofcomments)
print totalcount

#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
# 
#     print 'lat',lat,'lng',lng
#     print location

