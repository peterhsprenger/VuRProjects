import datetime

# Durch den Import der datetime-Library kann in einem Programm mit Datumswerten gearbeitet werden.

# Diese Funktion gibt das aktuelle Datum zurueck
heute = datetime.date.today()
print heute

# Diese Funktionen geben einzelne Elemente des Datums zurueck
heutejahr = datetime.date.today().year
heutejahr2 = heute.year
print heutejahr, heutejahr2
heutemonat = datetime.date.today().month
heutemonat2 = heute.month
print heutemonat, heutemonat2
heutetag = datetime.date.today().day
heutetag2 = heute.day
print heutetag, heutetag2

# Datumswerte muessen in verschiedenen Formaten ausgegeben werden koennen
# strftime allows to specify the date format - vgl. alle Optionen unter strftime.org - einige Beispiele:
heuteformat1 = heute.strftime('%d %b, %Y')
print 'heuteformat1', heuteformat1

heuteformat2 = heute.strftime('%d %B, %y')
print 'heutformat2', heuteformat2

heuteformat3 = heute.strftime('%a, %d %b %Y')
print 'heuteformat3', heuteformat3

heuteformat3 = heute.strftime('%A, %d %b %Y')
print 'heuteformat3', heuteformat3

# Fuer die Lokalisierung die Library babel.pocoo.org verwenden