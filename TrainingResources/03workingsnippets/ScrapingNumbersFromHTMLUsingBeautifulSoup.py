# - * - coding: iso-8859-1, utf-8 - * -
# Created on 01.11.2015 by @author: PeterH

import bs4import urllib2
from bs4 import BeautifulSoup
import lxml

persons = []
iterations = 7
iter = 1
follow = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Maura.html'
while iter <= iterations: 
    html = urllib2.urlopen(follow).read()
    soup = bs4.BeautifulSoup(html)
    tag = soup('a')[17]
    persons.append(tag.contents[0])
    follow = tag.get('href', None)
    print persons
    iter += 1
lastperson = persons[-1]
print lastperson




# 
# for tag in tags:
#     assignmentsum = assignmentsum + int(tag.contents[0])
# print assignmentsum