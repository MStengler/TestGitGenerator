import xml.etree.ElementTree as ET

def lade_xml(pfad):
    tree = ET.parse(pfad)
    root = tree.getroot()
    daten = []

    for element in root:
        eintrag = {child.tag: child.text for child in element}
        daten.append(eintrag)
    return daten
