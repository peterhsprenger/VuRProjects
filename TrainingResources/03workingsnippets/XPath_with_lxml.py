import urllib2
import lxml
from lxml import html

DNBPage = urllib2.urlopen('http://d-nb.info/gnd/4046049-6').read()
#DNBPage = open('C:/Users/PeterH/eclipsemars/TrainingResources/documents/X00testdocs/DNBportal_dnb_de_opac_htm_method=simpleSearch&cqlMode=true&query=idn=007.htm', 'r').read()
#print DNBPage

tree = html.document_fromstring(DNBPage)
#print tree

#print tree.xpath('*')
#print tree.xpath('node()')
#print tree.xpath('body')
#print tree.xpath('body/*')
#print tree.xpath('body/div/*')
#print tree.xpath('body/div/div/*')         # zeigt die Elemente unterhalb des ersten divs unterhalb des ersten divs unterhalb des body an
#print tree.xpath('//table/text()')         # zeigt den Text aller Tabellen an 
#print tree.xpath('//li/text()')            # zeigt den Text aller Elemente mit dem Tag <li>
#print tree.xpath('//@*')                   # zeigt alle Attribute der Seite an
#print tree.xpath('//table[@id="fullRecordTable"]')       # zeigt die Tabelle mit der ID "fullRecordTable"

print tree.xpath('//table/@id="fullRecordTable"')         
                    # Gibt true (oder false) aus, wenn eine Tabelle mit dieser ID existiert 
                    # (oder nicht existiert) und kann dementsprechend in einer Schleife 
                    # z.B. verwendet werden, um das Vorhandensein als Grundlage 
                    # eines bedingt auszufuehrenden Programmcodes zu pruefen

#print tree.xpath('//table[@id="fullRecordTable"]/text()')            # zeigt den Text der Tabelle mit der ID "fullRecordTable"

