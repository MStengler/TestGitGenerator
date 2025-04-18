import json

def lade_json(pfad):
    with open(pfad, encoding='utf-8') as f:
        return json.load(f)
