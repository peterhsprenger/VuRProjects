# um einen String mit einer Zahl auszugeben muss die Zahl in einen String umgewandelt werden.
# Eine Verknuepfung wie "Ich bin ein String " + Nummer ist nicht moeglich. 
# Es gibt zwei Moeglichkeiten:
# 1. Umwandlung einer Nummer in einen String:

nummer = 25
nummer2 = 10000
satz = "Die Nummer lautet: "
print satz + str(nummer)

# 2. Eine andere und flexiblere Variante ist das Einfuegen eines Platzhalters im String: 

print "Die Nummer %d ist durch 5 teilbar" % nummer     # setzt die Nummer anstelle des Platzhalter %d eingabe

# Ausserdem kann die Nummer mit Hilfe des Platzhalter formatiert werden:

# richtet die Zahl anhand der hinter dem %-Zeichen angegebenen Zeichenanzahl aus; 
# wenn also bis zu dreistellige Nummern erwartet werden, koennen die Zahlen dadurch in einer Kolonne ausgegeben werden
print "\n\nDie Nummer %6d ist durch 5 teilbar" % nummer
print "Die Nummer %6d ist durch 5 teilbar \n\n" % nummer2

# richtet die Zahl anhand der hinter dem %-Zeichen angegebenen Zeichenanzahl aus und setzt zusaetzlich eine fuehrende 0 davor 
# wenn also bis zu dreistellige Nummern erwartet werden, koennen die Zahlen dadurch in einer Kolonne ausgegeben werden
print "Die Nummer %03d ist durch 5 teilbar" % nummer    

# wandelt die Nummer in eine float-Zahl um, egal ob es sich vorher um eine float-Zahl handelte; 
# standardmaessig werden dann 6 Kommastellen ausgegeben
print "Die Nummer %f ist durch 5 teilbar" % nummer

# wandelt die Nummer in eine float-Zahl um, egal ob es sich vorher um eine float-Zahl handelte; 
# Es werden so viele Kommastellen ausgegeben, wie mit dem Signal . und der Zahl dahinter angegeben werden
print "Die Nummer %.2f ist durch 5 teilbar" % nummer


# Eine dritte Moeglichkeit ist die Verwendung einer format method:
print "\n\nDie Nummer {0:6d} ist durch 5 teilbar".format(nummer2)
print "Die Nummer {0:06d} ist durch 5 teilbar \n\n".format(nummer2)
print "Die Nummer {0:.4f} ist durch 5 teilbar".format(nummer)
print "Die Nummer {0:.2f} ist durch 5 teilbar".format(nummer)

#Diese Methode hat den Vorteil, dass man mehrere Werte uebergeben kann und genau festlegen kann, welche der Nummern angezeigt werden soll:
print "Die Nummer {1:06d} ist durch 5 teilbar \n\n".format(nummer, nummer2)

# ... oder mehrere Numemrn:
print "Die erste Nummer {0:06d} ist durch 5 teilbar, die zweite Nummer {1:d} auch \n\n".format(nummer, nummer2)

