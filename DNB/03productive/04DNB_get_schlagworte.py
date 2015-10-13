# -*- coding: iso-8859-1, utf-8 -*-
import re
import urllib2
from urllib2 import Request, URLError, HTTPError, urlopen
from pip._vendor.cachecontrol.controller import URI


# die folgenden Skripte geben zu einer ID der GND den Beschreibungstext aus

dnb_sachbegriffe = {}           # in diesem Dictionary werden die ISBNs als Key mit der DNB-ID als Value gespeichert
#dnb_topics = ['11853985X', '11906765X', '11890261X', '11926062X', '11872827X', '11856269X', '11558871X', '11657075X', '11872522X', '10412573X', '11857941X', '11864291X', '11859818X', '11859382X', '11853601X', '11864310X', '11860564X', '11853596X', '11853453X', '11854845X', '121357-X', '12872630X', '11855333X', '11724399X', '10351255-X', '4026779-9', '12469733X', '11901047X', '11913764X', '11932119X', '11865117X', '11906037X', '11850391X', '2022204-X', '11869569X', '11859740X', '11728257X', '2046311-X', '11948370X', '12231297X', '6031073-X', '11858314X', '11852786X', '11872780X', '11105799X', '11855817X', '11857521X', '11554609X', '11895122X', '11913988X', '11871404X', '11862136X', '11860354X', '11896903X', '11932816X', '11851024X', '11851282X', '11861214X', '11855042X', '11857938X', '11863562X', '11856322X', '11855896X', '1009152-X', '12447778X', '11860922X', '104855337X', '11862234X', '11880166X']             # in dieser Liste werden die Topics aus den DNB-Daten gespeichert
#inputfiles = ['F:/VLBGoldFiles/sourcefiles/clean9783525.txt', 'F:/VLBGoldFiles/sourcefiles/clean9783647.txt', 'F:/VLBGoldFiles/sourcefiles/clean97838252.txt', 'F:/VLBGoldFiles/sourcefiles/clean97838385.txt', 'F:/VLBGoldFiles/sourcefiles/clean97838470.txt', 'F:/VLBGoldFiles/sourcefiles/clean97838471.txt', 'F:/VLBGoldFiles/sourcefiles/clean978386234.txt', 'F:/VLBGoldFiles/sourcefiles/clean978389971.txt'] 
#inputfiles = ['F:/VLBGoldFiles/sourcefiles/clean97838252.txt'] 

inputpath = '${INPUT_DOCS}'
outputpath = '${INTERMEDIARY_DOCS}'
isbnprefixes = ['9783525' , '9783647' , '97838252' , '97838385' , '97838470' , '97838471' , '978386234' , '978389971']

def get_topic_list_from_dnb_download_files(source):
    gnd = []
    for src in source :        
        inp = inputpath & 'clean' & src & '.txt'
        out = outputpath + 'topicID_' + src + '.txt'
        finp = open(inp)        
        finp.read()
        gnd = re.findall('dcterms:subject rdf:resource="http://d-nb\.info/gnd/([0-9-X]+)', finp) 

        for topic in gnd:
            if topic not in dnb_topics :
                dnb_topics.append(topic)
            else :
                continue
    print dnb_topics 


def parse_DNBsite_for_topics(Liste):
    counter = 0
    for topic in Liste :
        urlline = 'http://d-nb.info/gnd/' + topic
        print urlline
        req = Request(urlline)
        try: 
            response = urlopen(req).read()
            if re.search('<strong>Sachbegriff</strong>', response) is not None:
                print "Sachbegriff"
                sachbegriff = re.findall('Sachbegriff</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            elif re.search('<strong>Person</strong>', response) is not None: 
                print "Person"
                sachbegriff = re.findall('Person</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            elif re.search('<strong>Geografikum</strong>', response) is not None: 
                print "Geografikum"
                sachbegriff = re.findall('Geografikum</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            elif re.search('<strong>Titel des Werkes</strong>', response) is not None: 
                print "Titel des Werkes"
                sachbegriff = re.findall('Titel des Werkes</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            elif re.search('<strong>Person\(en\)</strong>', response) is not None: 
                print "Person(en)"
                sachbegriff = re.findall('Person\(en\)</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)    
            elif re.search('<strong>Organisation</strong>', response) is not None:  
                print "Organisation"
                sachbegriff = re.findall('Organisation</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            elif re.search('<strong>Veranstaltung</strong>', response) is not None:  
                print "Veranstaltung"
                sachbegriff = re.findall('Veranstaltung</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            else :
                print "unbekannt"
                sachbegriff = 'unbekannt'
            print sachbegriff
        
            dnb_sachbegriffe[topic] = sachbegriff

        except HTTPError, e:
            sachbegriff = ['ERROR: The server could not fulfill the request.']
            dnb_sachbegriffe[topic] = sachbegriff
            #print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError, e:
            sachbegriff = ['ERROR: We failed to reach a server.']
            dnb_sachbegriffe[topic] = sachbegriff
            #print 'We failed to reach a server.'
            print 'Reason: ', e.reason            
        counter = counter + 1
        print 'Iteration', counter
    print dnb_sachbegriffe


def print_and_save_dictionary_items(dictionary):
    results = open(outputfile, 'w')
    count = 0
    for k, v in dnb_sachbegriffe.items(): 
        try:
            count += 1
            print '-'*70
            print 'EINTRAG NR. ' + str(count)
            print 'GND-ID: ', k
            print '0 - Begriff: ', v
            print 
            
            # mit dieser Methode werden die Daten ausserdem in eine Datei ausgegeben
            datatowrite = k + '|' + str(v) + '\n'
            results.write(datatowrite)
        except:
            pass
    
    results.write(str(count) + " Einträge")
    print "Das Dictionary hat", len(dnb_sachbegriffe), "Einträge" 



get_topic_list_from_dnb_download_files(isbnprefixes)
#parse_DNBsite_for_topics(dnb_topics)
#print_and_save_dictionary_items(dnb_sachbegriffe)
