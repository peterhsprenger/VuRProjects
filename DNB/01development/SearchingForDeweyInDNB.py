# -*- coding: iso-8859-1, utf-8 -*-
# Created on 05.11.2015 by @author: PeterH 

base_file = 'C:\Users\PeterH\eclipsemars\DNB\documents\X03finalresults\dictDNB_9783647complete.txt'
finp = open(base_file)
finpeval = eval(finp.read())

for isbn in finpeval:
    ddc_min = '791'
    ddc_max = '792'
    for ddccode in finpeval[isbn][4]:
        if str(ddccode) >= ddc_min and str(ddccode) < ddc_max:
            print isbn, '-', str(ddccode)
        else:
            pass

