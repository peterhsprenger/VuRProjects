# -*- coding: iso-8859-1, utf-8 -*-
# Created on 31.10.2015 by @author: PeterH 
import re

inputfile = 'C:\\Users\\PeterH\\eclipsemars\\TrainingResources\\documents\\X00testdocs\\regex_sum_189082.txt'

regexfile = open(inputfile).read()
numberlist = re.findall('[0-9]+', regexfile)

numbersum = 0 
for number in numberlist:
    numbersum = numbersum + int(number)
print numbersum