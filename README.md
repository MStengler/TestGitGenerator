# TestGitGenerator

# Die sichere Git-Strategie vor jedem Push:

# 1. Hol die neuesten Änderungen (immer!)
git pull --rebase origin main

# 2. Mach deine Änderungen lokal
# z. B. neue Datei, Code ergänzt …

# 3. Speichere sie mit Commit
git add .
git commit -m "Mein neuer Code"

# 4. Lade sie hoch
git push

✅ Mit alt + f12 local Terminal öffnen
📍 Öffne das Terminal in PyCharm:
Unten im Fenster Terminal anklicken (oder Alt + F12 drücken)

📥 Dann diesen Befehl eingeben (je nach Dateinamen):

python main.py --eingabe testdaten/testdaten.json --ausgabe output/turingmaschine.png --format json --config konfig/beispiel_config.json

Achte genau auf:
Pfadnamen: stimmen die Dateinamen in testdaten/, konfig/ und output/?
Groß-/Kleinschreibung bei Windows ist meistens tolerant, trotzdem besser korrekt

📦 Was passiert?
testdaten/testdaten.json wird geladen
konfig/beispiel_config.json bestimmt Farben, Logo, Prof
Die Grafik wird als output/turingmaschine.png erzeugt

📁 Danach:
Gehe in deinen Projektordner → output/
Öffne die Datei turingmaschine.png (z. B. mit Doppelklick)

