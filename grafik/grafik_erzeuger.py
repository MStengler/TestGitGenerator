import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from PIL import Image
import os

def erstelle_modulgrafik(daten, ausgabe_pfad, konfig={}):
    # Basisdaten
    modul = daten.get("modulname", "Modul")
    dauer = daten.get("dauer", "00:00")
    aufgaben = daten.get("aufgaben", "0")
    zieltext = daten.get("lernziel", "Zielbeschreibung folgt...")

    # Konfiguration
    farbe = konfig.get("farbe", "#007fff")
    titel = konfig.get("titel", "Modulübersicht")
    xlabel = konfig.get("xlabel", "")
    ylabel = konfig.get("ylabel", "")
    logo_pfad = konfig.get("logo", None)
    prof_pfad = konfig.get("professor", None)
    bildform = konfig.get("bildform", "rechteck")

    # Grafik-Grundfläche
    # Auflösung aus Konfig (Standard: 12x7 Zoll bei 100 dpi = 1200x700)
    width, height = konfig.get("auflösung", [1200, 700])
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))
    ax.axis("off")

    # Hintergrundfarbe
    hintergrundfarbe = konfig.get("hintergrund", "white")
    fig.patch.set_facecolor(hintergrundfarbe)

    # Titel und Modulname
    ax.text(0.05, 0.9, titel.upper(), fontsize=18, color=farbe, weight="bold", transform=ax.transAxes)
    ax.text(0.05, 0.82, modul.upper(), fontsize=26, color="black", weight="bold", transform=ax.transAxes)

    # Dauer, Aufgaben
    ax.text(0.05, 0.72, f"⏱️ {dauer}", fontsize=14, transform=ax.transAxes)
    ax.text(0.25, 0.72, f"📄 {aufgaben} Aufgaben", fontsize=14, transform=ax.transAxes)

    # Ziel
    ax.text(0.05, 0.6, "🎯 " + zieltext, fontsize=14, wrap=True, transform=ax.transAxes)

    # THWS-Logo
    if logo_pfad and os.path.exists(logo_pfad):
        img = mpimg.imread(logo_pfad)
        logo_position = konfig.get("logo_position", "standard")

        if logo_position == "oben_links":
            # Links oben – wie bei THWS
            ax.imshow(img, extent=[0.02, 0.12, 0.86, 0.98], transform=ax.transAxes, zorder=10)
        else:
            # Standard-Position (oben rechts)
            ax.imshow(img, extent=[0.8, 0.95, 0.88, 0.97], transform=ax.transAxes, zorder=10)

    # Professorenbild
    if prof_pfad and os.path.exists(prof_pfad):
        img = Image.open(prof_pfad).convert("RGBA")
        if bildform == "rund":
            size = img.size
            mask = Image.new('L', size, 0)
            draw = Image.new('RGBA', size)
            for y in range(size[1]):
                for x in range(size[0]):
                    if (x - size[0]/2) ** 2 + (y - size[1]/2) ** 2 < (min(size)/2) ** 2:
                        mask.putpixel((x, y), 255)
            img.putalpha(mask)
        img = img.resize((150, 150))
        ax.imshow(img, extent=[0.8, 0.95, 0.1, 0.35], transform=ax.transAxes, zorder=9)

    # Speichern
    plt.savefig(ausgabe_pfad, dpi=300, bbox_inches="tight")
    plt.close()
