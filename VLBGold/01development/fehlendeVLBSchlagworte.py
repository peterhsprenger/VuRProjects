# -*- coding: iso-8859-1, utf-8 -*-
# Created on 14.10.2015 by @author: PeterH 

isbn_kw_dict = {}

inputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//ddcabgleich647.txt"
sourcefile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//dictDNB_9783647complete.txt"
outputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X03finalresults//ddcabgleich647.txt"


def create_dictionary(inp, out):
    finp = open(inp)        
    finpeval = eval(finp.read())
    fsrc = open(out)        
    fsrceval = eval(fsrc.read())
    
    for isbn in finpeval:
        try:
            isbn_kw_dict[isbn] = fsrceval[isbn][4]
            #print isbn, fsrceval[isbn][8]
        except:
            isbn_kw_dict[isbn] = ["ISBN nicht bei DNB vorhanden"]
            #print isbn, "nicht vorhanden"

    print isbn_kw_dict
    print "*" * 50

    
def print_and_save_dictionary_items(dictionary):
    results = open(outputfile, 'w')
    count = 0
    for k, v in dictionary.items(): 
        try:
            count += 1
            print '-'*70
            print 'EINTRAG NR. ' + str(count)
            print 'ISBN: ', k
            print 'DDC: ', v
            print 
            
            # mit dieser Methode werden die Daten in die Datei ausgegeben
            datatowrite = k + ';' + str(v) + '\n'
            results.write(datatowrite)
        except:
            pass    

create_dictionary(inputfile, sourcefile)
print_and_save_dictionary_items(isbn_kw_dict)