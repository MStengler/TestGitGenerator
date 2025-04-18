import argparse
import os
import sys

from parser.csv_parser import lade_csv
from parser.json_parser import lade_json
from parser.xml_parser import lade_xml
from grafik.grafik_erzeuger import erstelle_modulgrafik

def zeige_first_frame():
    print(r"""
███████╗████████╗██╗   ██╗██████╗ ██╗███████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔════╝
███████╗   ██║   ██║   ██║██████╔╝██║█████╗  
╚════██║   ██║   ██║   ██║██╔═══╝ ██║██╔══╝  
███████║   ██║   ╚██████╔╝██║     ██║███████╗
╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝

📊 Studiengrafik Generator v1.0

Ein Tool zur Erstellung THWS-ähnlicher Grafiken auf Basis von strukturierten Daten.

Verwendung:
  python main.py --eingabe datei.json --ausgabe grafik.png --format json --config konfig.json

Parameter:
  --eingabe     Pfad zur Eingabedatei (csv, json, xml)
  --ausgabe     Pfad zur Ausgabedatei (z. B. grafik.png)
  --format      Eingabeformat: csv | json | xml
  --config      Optional: Konfigurationsdatei (Farben, Logo, Professorenbild)
    """)

def parse_args():
    parser = argparse.ArgumentParser(description="Studiengrafik Generator")
    parser.add_argument("--eingabe", type=str, help="Pfad zur Eingabedatei")
    parser.add_argument("--ausgabe", type=str, help="Pfad zur Ausgabegrafik")
    parser.add_argument("--format", type=str, choices=["csv", "json", "xml"], help="Eingabeformat")
    parser.add_argument("--config", type=str, help="Optional: JSON-Konfigurationsdatei")
    return parser.parse_args()

def einlesen_daten(format, pfad):
    if format == "csv":
        return lade_csv(pfad)
    elif format == "json":
        return lade_json(pfad)
    elif format == "xml":
        return lade_xml(pfad)
    else:
        raise ValueError(f"❌ Unbekanntes Format: {format}")

def main():
    args = parse_args()

    if not any(vars(args).values()):
        zeige_first_frame()
        sys.exit(0)

    if not os.path.exists(args.eingabe):
        print("❌ Die Eingabedatei wurde nicht gefunden.")
        sys.exit(1)

    print("📥 Lese Daten...")
    daten = einlesen_daten(args.format, args.eingabe)

    if isinstance(daten, list):
        # Verwende den ersten Eintrag, falls Liste
        daten = daten[0]

    konfig = {}
    if args.config:
        if os.path.exists(args.config):
            konfig = lade_json(args.config)
        else:
            print("⚠️ Konfigurationsdatei nicht gefunden. Es werden Standardwerte genutzt.")

    print("🖼️ Erzeuge Grafik...")
    erstelle_modulgrafik(daten, args.ausgabe, konfig)

    print(f"✅ Grafik gespeichert unter: {args.ausgabe}")

if __name__ == "__main__":
    main()
