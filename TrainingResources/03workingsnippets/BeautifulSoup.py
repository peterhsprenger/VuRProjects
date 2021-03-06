# -*- coding: utf-8 -*-

import bs4
from bs4 import BeautifulSoup
import urllib2
import os
import sys
import lxml 
import re

schlagwort = ['erstes Schlagwort', 'Zweites Schlagwort']

#DNBPage = urllib2.urlopen('http://d-nb.info/gnd/4011890-3').read()   #('http://d-nb.info/gnd/2065138-7')
DNBPage = urllib2.urlopen('http://d-nb.info/gnd/4046049-6').read()

#DNBPage = open('C:/Users/PeterH/eclipsemars/TrainingResources/documents/X00testdocs/DNBportal_dnb_de_opac_htm_method=simpleSearch&cqlMode=true&query=idn=007.htm', 'r')

# Einlesen des Quelltextes mit Beautiful Soup und Ausdruck der kompletten Seite
soup = BeautifulSoup(DNBPage, 'lxml')
#print soup.prettify()


#  Ausdruck der Seite in der Optik der Baumstruktur
#print soup.prettify()


# Ausdruck nur des Textes der Seite, ohne Tags
#print soup.get_text()


# Ausdruck aller Links auf der Seite
# for link in soup.find_all('a'):
#     print link.get('href')


# findet die komplette Tabelle mit der ID 'fullRecordTable' und macht aus dem kompletten String eine Liste   
tableContent = soup.find('table', {'id' : 'fullRecordTable'})
#print tableContent.prettify()
DNBResult = tableContent.findNext().findNextSibling().findNextSibling().findNext().findNextSibling().get_text()
#print DNBResult, type(DNBResult)
finalResult = re.findall('\t*([A-Za-z0-9-\.,]+)', DNBResult)
#print finalResult
schlagwort.append(finalResult[0])
print schlagwort
print schlagwort[2]


# Findet in der kompletten "soup" alle Elemente mit dem Tag <tr> und legt sie in einer Liste ab
rows = soup.find_all('tr')
# print rows
# print type(rows)
# druckt statt der kompletten "rows" die "rows" mit dem Index 2, also das dritte Element mit dem Tag <tr> 
# das Ergebnis dieser Angabe eines Indexes ist ein String, nicht mehr eine Liste
# print rows[2]
# print type(rows[2])
# druckt vom gleichen Ergebnis nur den Text
#print rows[2].get_text()


# findet die Elemente mit dem Tag <td> in dem selektierten Element rows[2] - 
# rows[2] ist ein String, columns ist wiederum eine Liste
# columns = rows[2].find_all('td')
# columnsgt = columns[1].get_text()
# print columnsgt
# print type(columnsgt)


# findet den Titel der Seite 
#print soup.title


# findet den Head der Seite 
# print soup.head

# findet den Body der Seite 
# print soup.body

# sTable = soup.table
#print sTable

# sTr = sTable.find_all('tr')[2]
#print sTr

# sTd = sTr.find_all('td')[1]
#sTdgt = sTd.get_text()
# sTdgt = sTd.prettify()
# sTdgtp = sTd.get_text()
# print sTdgtp


