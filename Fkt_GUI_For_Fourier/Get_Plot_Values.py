"""
Berechnet für alle x-Werte in einer Periode die y-Werte für das Polynom und die Fourierreihe.
values[0] - x-Werte (Zeit in h)
values[1] - Durchschnittswerte der Rohdaten
values[2] - Zu berechnende Werte des Polynoms
values[3] - Zu berechnende Werte der Fourierreihe
"""

import numpy as np
import sympy as sp
import math as m

def Get_Plot_Values (data):
    values = np.array([[0.0]*len(data[0][0])]*4)                        # Initiiert den Array für die X- und Y-Werten zu allen Funktionen
    values[0] = np.array(data[0][0])                                    # Die X-Werte bestehen aus den Stunden aus den Rohdaten und werden übernommen
    values[1] = np.array(data[0][1])                                    # Die Werte der Durchschnittswerte werden übernommen
    for i, x in enumerate(values[0]):
        for j, coefficient in enumerate(data[1]):
            values[2][i] += coefficient[0] * x**j                       # Berechnung der Werte des Polynoms
        values[3][i] += data[2][0][0]/2                                 # Berechnung der Werte vom a0/2 Summanden
        for j in range(1, len(data[2])):                  # Berechnung der Werte der Fourierreihe
            values[3][i] += data[2][j][0] * m.cos(sp.pi*2/24*x*j) + data[2][j][1] * m.sin(2*sp.pi/24*x*j)   # Berechnung der Werte der weiteren Summanden Summanden
    return values