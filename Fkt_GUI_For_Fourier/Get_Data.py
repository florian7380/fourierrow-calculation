"""
Im Folgenden wird eine Datei von der Bundesnetzagentur mit den Leistungswerten eingelesen, 
welche dann als Funktion genähert und als zweite NJäherung durch eine Fourierreihe angegeben werden.
Eingegeben werden Werte zur Genauigkeit der Näherungen. Das sind:
1. die Anzahl der Punkte, die aus den Durchschnittswerten aus der Datei berechnet werden 
und auf dessen Grundlage ein Gleichungssystem erstellt wird, dass dann zum Polynom führt
2. Die Anzahl zu berechnender Fourierkoeffizienten, die dann zur Fourierreihe führen.
"""

import csv
import numpy as np

import Fkt_GUI_For_Fourier.Fkt_Get_Data as fkt


"""
Vorbereitung für die Fourierkoeffizienten
- Datenaufnahem und -verarbeitung
- Bildung der Funktion (Polynom), als Näherung an durchschnittliche Daten eines Tages der Rohdaten
"""


def Get_Data (var, osz, link):
    link.replace(r'\\','/')
    with open('C:/Users/flori/Documents/Tabellen_Daten__202308080000_202308102359/Realisierter_Stromverbrauch_202310090000_202310112359_viertelstunde.csv') as csv_data:      # Lädt die Datei des Pfades
        raw_data = list(csv.reader(csv_data, delimiter=";"))        # Teilt die Werte in eine Matrix auf
    
    data = np.array([None, None])
    
    for i, e in enumerate(raw_data):
        data = np.vstack((data, [e[1], e[3]]))  # Nimmt die Daten für Zeit und Leistung in die Matrix auf
    
    data = np.delete(data, 0, 0)                # Löscht die erste Zeile, da sie nur Bezeichnungen beinhaltet
    data = np.delete(data, 0, 0)                # Löscht die zweite Zeile, da sie nur die Einheiten beinhaltet
    
    data = fkt.Change_Time_Format(data)             # Schreibt die Zeit von hh:mm in x.xx h um
    
    n_period = fkt.Number_Of_Values_In_Period(data) # Zählt die Anzahl Werte in einer Periode

    av_data = fkt.Calc_AV_Data(n_period, data)      # Berechnung der durchschnittlichen Werte einer Periode (Eines Tages)

    points = fkt.Calc_Points(n_period, var, av_data)    # Berechnen der Punkte für die Polynombildung
    
    calc = fkt.Form_Poly(points)                    # Bildet aus den Punkten ein Polynom
    
    """
    Berechnung der Fourierkoeffizienten in der Form:
    a0  b0
    a1  b1
    a2  b2
    .
    .
    .
    übergeben wird das Polynom, die Nummer des Koeffizienten, ob es koeffizient a (0) oder b (1) ist und wie lange die Periode ist.
    """
    
    fourier_koef = np.array([[None] * 2] * osz)
    for i in range(osz):                                                    # Geht die Nummer der Koeffizienten durch
        for j in range(2):                                                  # wechselt zwischen 0 un 1 um Parameter a und b zu bestimmen
            fourier_koef[i][j] = fkt.Calc_Fourierkoefficient(calc, i ,j, 24)     # Speichert Berechnet die unterschiedlichen Fourierkoeffizienten
    values_return = np.array([None]*3)                                      # Matrix für alle alle benötigt Werte
    values_return[0] = np.array(av_data)
    values_return[1] = np.array(calc)
    values_return[2] = np.array(fourier_koef)
    return values_return