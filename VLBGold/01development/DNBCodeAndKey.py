# -*- coding: iso-8859-1, utf-8 -*-
# Created on 19.10.2015 by @author: PeterH 


isbn_kw_dict = {}

inputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//VLBReport_VuR_ohneSchlagworte_LIST.txt"
sourcefile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X01inputdocs//DNBComplete_DICT.txt"
outputfile = "C://Users//PeterH//eclipsemars//VLBGold//documents//X03finalresults//NAVImport_ISBN_Schlagworte.txt"

id_kw_dict = {}

def create_dictionary(inp):
    finp = open(inp)        
    finpeval = eval(finp.read())
    
    for isbn in finpeval:
        iter = len(finpeval[isbn][3])
        i = 0
        id_kw_list = [] 
        while i <= iter:
            try :
                print finpeval[isbn][3][i]  
                print finpeval[isbn][8][i]
                id_kw_list.append(finpeval[isbn][3][i])
                id_kw_list.append(finpeval[isbn][3][i])
            except: pass 
            i = i + 1
        finpeval[isbn] = id_kw_list
    print id_kw_dict        

    
def print_and_save_dictionary_items(outputfile):
    results = open(outputfile, 'w')
    count = 0
    for k, v in id_kw_dict.items(): 
        try:
            count += 1
            print '-'*70
            print 'EINTRAG NR. ' + str(count)
            print 'ID: ', k
            print 'KW: ', v
            print 
            
            # mit dieser Methode werden die Daten in die Datei ausgegeben
            datatowrite = k + '\t' + str(v) + '\n'
            results.write(datatowrite)
        except:
            pass    

create_dictionary(inputfile)
#print_and_save_dictionary_items(outputfile)

