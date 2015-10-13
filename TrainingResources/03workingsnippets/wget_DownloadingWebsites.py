import os.system
import wget

os.system('wget --convert-links --no-clobber --wait=4 --limit-rate=10K -r --no-parent --http://d-nb.info/gnd/')

# Nach Installation von wget werden alle HTML-Seiten der angegebenen URL heruntergerladen.
# der Parameter wait sorgt dafuer, dass die Anfragen nicht zu schnell gestellt werden
# Besonders wichtig ist der Parameter no-parent, der verhindert, dass der Download auch auﬂerhalb
# der angegebenen URL fortgesetzt wird - wird er nicht angegeben, kann es passieren, dass Links
# zu groﬂen Webseiten fuehren, die dann ebenfalls heruntergeladen werden (facebook, Spiegel usw.)



