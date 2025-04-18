import csv

def lade_csv(pfad):
    with open(pfad, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        daten = [row for row in reader]
    return daten
