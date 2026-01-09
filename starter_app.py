import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    # Weitere Imports hier ergänzen (z.B. plotly)
    return mo, pd


@app.cell
def __(mo):
    mo.md(
        r"""
        # 🌱 Ökobilanz-App für Erneuerbare Energien
        
        **Entwickelt von: [EUER GRUPPENNAME]**
        
        Kurze Beschreibung eurer App hier einfügen...
        
        ---
        """
    )
    return


@app.cell
def __(pd):
    # =================================================================
    # DATEN
    # =================================================================
    # Hier eure Daten einfügen
    # 
    # Tipp: Recherchiert auf https://www.probas.umweltbundesamt.de
    # 
    # Beispielstruktur:
    # energietraeger_daten = pd.DataFrame({
    #     "Energieträger": ["Photovoltaik", "Windkraft", ...],
    #     "CO2_eq_g_kWh": [40, 10, ...],
    #     ...
    # })
    
    # TODO: Eure Daten hier einfügen
    energietraeger_daten = pd.DataFrame({
        "Energieträger": ["Beispiel 1", "Beispiel 2"],
        "CO2_eq_g_kWh": [0, 0],
        # Weitere Spalten ergänzen...
    })
    
    return (energietraeger_daten,)


@app.cell
def __(energietraeger_daten, mo):
    # =================================================================
    # BENUTZEROBERFLÄCHE (UI)
    # =================================================================
    # Hier interaktive Elemente erstellen
    #
    # Beispiele:
    # - Dropdown: mo.ui.dropdown(options=[...], label="...")
    # - Slider:   mo.ui.slider(start=0, stop=100, value=50, label="...")
    # - Checkbox: mo.ui.checkbox(label="...")
    #
    # Dokumentation: https://docs.marimo.io/api/inputs/
    
    # TODO: Eure UI-Elemente hier erstellen
    
    # Beispiel Dropdown:
    energie_auswahl = mo.ui.dropdown(
        options=energietraeger_daten["Energieträger"].tolist(),
        value=energietraeger_daten["Energieträger"].iloc[0],
        label="Energieträger auswählen"
    )
    
    # Beispiel Slider:
    # leistung_slider = mo.ui.slider(start=1, stop=1000, value=100, label="Leistung (kW)")
    
    return (energie_auswahl,)


@app.cell
def __(energie_auswahl, mo):
    # UI-Elemente anzeigen
    mo.md(f"""
    ## ⚙️ Parameter
    
    {energie_auswahl}
    
    """)
    return


@app.cell
def __(energie_auswahl, energietraeger_daten):
    # =================================================================
    # BERECHNUNGEN
    # =================================================================
    # Hier die Berechnungen basierend auf der Auswahl durchführen
    #
    # Beispiel:
    # ausgewaehlter_traeger = energie_auswahl.value
    # daten = energietraeger_daten[energietraeger_daten["Energieträger"] == ausgewaehlter_traeger]
    # co2_wert = daten["CO2_eq_g_kWh"].iloc[0]
    
    # TODO: Eure Berechnungen hier
    
    ausgewaehlter_traeger = energie_auswahl.value
    
    # Beispiel: Daten für ausgewählten Träger holen
    daten = energietraeger_daten[
        energietraeger_daten["Energieträger"] == ausgewaehlter_traeger
    ].iloc[0]
    
    return ausgewaehlter_traeger, daten


@app.cell
def __(ausgewaehlter_traeger, daten, mo):
    # =================================================================
    # ERGEBNISSE ANZEIGEN
    # =================================================================
    # Hier die Ergebnisse darstellen
    #
    # Beispiel:
    # mo.md(f"""
    # ## Ergebnisse für {ausgewaehlter_traeger}
    # 
    # | Kennzahl | Wert |
    # |----------|------|
    # | CO₂-Äquivalente | {wert} g/kWh |
    # """)
    
    # TODO: Eure Ergebnisdarstellung hier
    
    mo.md(f"""
    ## 📊 Ergebnisse für {ausgewaehlter_traeger}
    
    | Kennzahl | Wert |
    |----------|------|
    | CO₂-Äquivalente | **{daten['CO2_eq_g_kWh']}** g CO₂-eq/kWh |
    
    *Weitere Kennzahlen hier ergänzen...*
    """)
    return


@app.cell
def __(mo):
    # =================================================================
    # VISUALISIERUNG
    # =================================================================
    # Hier Diagramme erstellen
    #
    # Möglichkeiten:
    # - plotly: Interaktive Diagramme (empfohlen)
    #   import plotly.express as px
    #   fig = px.bar(df, x="...", y="...")
    #   mo.ui.plotly(fig)
    #
    # - matplotlib: Statische Diagramme
    #   import matplotlib.pyplot as plt
    #   plt.bar(...)
    #   plt.gcf()
    #
    # Dokumentation: https://docs.marimo.io/api/plotting/
    
    # TODO: Eure Visualisierungen hier
    
    mo.md("""
    ## 📈 Visualisierung
    
    *Hier kommen eure Diagramme hin...*
    """)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        
        ## ℹ️ Hinweise
        
        **Datenquellen:**
        - [Hier eure Quellen angeben]
        
        **Methodik:**
        - [Hier eure Methodik beschreiben]
        
        ---
        
        *Entwickelt für die Fachschule für Umweltschutztechnik*
        """
    )
    return


if __name__ == "__main__":
    app.run()
