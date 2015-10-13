import sys

firstno = raw_input('enter a number ')
secondno = raw_input('enter a number ')

try :
    result = float(firstno) / float(secondno)
    print result
except ZeroDivisionError:
    error = sys.exc_info() #[0]         # gibt eine konkretere Fehlermeldung aus, 
                                        # die sich auch zur Fehleranalyse eignet
                                        # mit Angabe der [0] wird nur der erste Teil der Fehlermeldung ausgegeben
    print 'Division by 0'
    print error

except ValueError:
    error = sys.exc_info()         
    print 'Wrong data type'
    print error
