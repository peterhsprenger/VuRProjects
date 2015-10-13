import csv
from _sqlite3 import Row

CSVFile = 'vlb-unipress.csv'
# myCSVFile = open(CSVFile, 'r')
# dataFromFile = csv.reader(myCSVFile, delimiter = ';')
# 
# print dataFromFile

with open(CSVFile, 'r') as myCSVFile : 
    dataFromFile = csv.reader(myCSVFile, delimiter = ';')
    for dataLine in dataFromFile :          # liefert eine Liste für jede Zeile der CSV-Datei
#        print dataLine
        print('|'.join(dataLine))
        for data in dataLine : 
#            print data
        
#print dataFromFile