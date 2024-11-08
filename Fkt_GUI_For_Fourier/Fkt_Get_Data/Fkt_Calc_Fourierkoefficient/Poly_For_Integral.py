"""
Bildet die Koeffizienten eines Polynoms und dessen Ableitungen als Array.
Benötigt wird:
Die Koeffizienten des Anfangspolynom als Matrix in der 1 Spalte
die n-te Ableitung
"""

import numpy as np

import Fkt_GUI_For_Fourier.Fkt_Get_Data.Fkt_Calc_Fourierkoefficient.Fkt_Poly_For_Integral as fkt


def Poly_For_Integral(polykoef, n):                           # poly_koef übegribt die Koeffizienten des Polynoms, n die Information der n-ten Ableitung, die für das Integral benötigt wird
    factorsforpoly = np.array([None] * len(polykoef))       # Matrix für verschiedene Werte die für die Berechnung des Polynoms benötigt werden
    degpoly = len(factorsforpoly)-1                         # Grad des Polynoms
    for i, e in enumerate(factorsforpoly):
        factorsforpoly[degpoly-i] = polykoef[degpoly-i][0]                  # Der Faktor des Ursprungspolynoms wird übernommen
        if degpoly-i >= n:                     # Prüfung ob der Summand überhaupt noch existiert bei der n-ten Ableitung, wenn ja dann nächste Zeile.
            factorsforpoly[degpoly-i] *= fkt.Faculty(degpoly-i)/fkt.Faculty(degpoly-i-n)    # Hinzumultiplizieren der Faktoren, wie sie bei der entsprechenden Ableitung hinzu kommen.
        else:
            factorsforpoly[degpoly-i] = 0.0                         # Faktoren die durch die Ableitung weg fallen werden 0 gesetzt
    return factorsforpoly