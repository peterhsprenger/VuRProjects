import glob        # die Library GLOB listet alle Dateien in einem Folder auf


#mit glob kann auf die Schnelle eine Liste aller Dateien in einem Ordner erstellt werden.

fileList = []
for f in glob.glob('C:/Users/PeterH/eclipsemars/DNB/documents/X01inputdocs/*.txt'):
    fileList.append(f)
     
print fileList