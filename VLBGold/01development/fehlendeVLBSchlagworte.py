# -*- coding: iso-8859-1, utf-8 -*-
# Created on 14.10.2015 by @author: PeterH 

isbn_kw_dict = {}

inputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//VLBReport_VuR_ohneSchlagworte_LIST.txt"
sourcefile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//DNBComplete_DICT.txt"
outputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X03finalresults//NAVImport_ISBN_Schlagworte.txt"


def create_dictionary(inp, src):
    finp = open(inp)        
    finpeval = eval(finp.read())
    fsrc = open(src)        
    fsrceval = eval(fsrc.read())
    
    for isbn in finpeval:
        try:
            iter = len(fsrceval[isbn][3])
            i = 0
            id_kw_list = []
            while i <= iter:
                (gnd, kw, count) = (fsrceval[isbn][3][i], fsrceval[isbn][8][i], i)
                id_kw_list.append((gnd, kw, (count+1)*10000))
                #(id_kw_list.append(fsrceval[isbn][3][i]), id_kw_list.append(fsrceval[isbn][8][i]))
                i = i + 1
        except: pass 
        isbn_kw_dict[isbn] = id_kw_list
    #print isbn_kw_dict['9783647367132'][1][1]

    
def print_and_save_dictionary_items(dictionary):
    results = open(outputfile, 'w')
    count = 0
    for isbn, gnd_kw_list in dictionary.items(): 
        for gnd_kw in gnd_kw_list:
            try:
                count += 1
                print '-'*70
                print 'EINTRAG NR. ' + str(count)
                print 'ISBN: ', isbn
                print 'gnd: ', gnd_kw[0], '| kw: ', gnd_kw[1], '| Z�HLER: ', gnd_kw[2] 
                print
                # mit dieser Methode werden die Daten in die Datei ausgegeben
                #datatowrite = isbn + '\t' + 'VLB' + '\t' + 'VLB-Schlagworte' + '\t' + gnd_kw[0] + '\t' + gnd_kw[1] + '\t' + gnd_kw[2] + '\n'
                #results.write(datatowrite)
            except:
                pass    
            datatowrite = isbn + '\t' + 'VLB' + '\t' + 'VLB-Schlagworte' + '\t' + gnd_kw[0] + '\t' + gnd_kw[1] + '\t' + str(gnd_kw[2]) + '\n'
            results.write(datatowrite)

create_dictionary(inputfile, sourcefile)
print_and_save_dictionary_items(isbn_kw_dict)