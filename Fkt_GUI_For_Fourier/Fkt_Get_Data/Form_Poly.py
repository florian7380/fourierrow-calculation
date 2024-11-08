""" Start der Polynombildung"""
    
    
    
"""
Macht aus den übergebenen Punkten eine Matrix der Form:
y1 a0*x1^0 a1*x1^1 a2*x1^2 ...
y2 a0*x2^0 a1*x2^1 ...
.
.
.

die dann in die Form 
bringt die Matrix in die Form:
    
w1      1       0       0       0 ...
w2      0       1       0       0 ...
w3      0       0       1       0 ...
.
.
.

sodass die erste Spalte die Vorfaktoren in der Reihenfolge a0 a1 a2 ... von oben nach unten bilden.
"""

import numpy as np

def Form_Poly(points):
    calc = np.array([[None]*(len(points[0])+1)]*len(points[0]))           # Matrix um die Werte des Polynoms zu speichern
     
    """
    Macht aus den übergebenen Punkten eine Matrix der Form:
        y1 a0*x1^0 a1*x1^1 a2*x1^2 ...
        y2 a0*x2^0 a1*x2^1 ...
        .
        .
        .
    """
    
    
    for i, e in enumerate(calc):                    # Hier wird ein Gleichungssystem in die Matrix gespeichert um die einzelnen Koeffizienten in der Matrix auszurechnen
        calc[i][0] = points[1][i]                   # Übernahme des y-Werts
        for j in range(1, len(calc[i])):
            calc[i][j] = points[0][i]**(j-1)        # Berechnung der einzelnen Werte mit vorgegebenen x-Wert in der passenden Potenz

    """
    bringt die Matrix in die Form:
        w1      1       a01     a02     a03 ...
        w2      0       1       a12     a13 ...
        w3      0       0       1       a23 ...
        .       
        .
        .
    """
    
    
    for i in range(len(calc)):                                      # zählt die Reihe und Spalte, Spalte mit i+1 für deb aktuell zu betrachtenden Koeffizienten, der den Vorfaktor 1 bekommen soll
        divisor = calc[i][i+1]                                      # speichert den aktuellen Wert, durch den geteilt werden muss, da dieser auch verändert wird
        for j in range(len(calc[0])):                               # zählt die Spalten, die dividiert werden um den Vorfaktor eines Koef 1 zu setzen
            calc[i][j] = calc[i][j]/divisor                         # teilt die gesamte reihe durch den Vorfaktor des aktuellen Koef
        for l in range(i+1, len(calc)):                             # zählt die Reihe bei der der Koef eingesetzt wird
            factor = calc[l][i+1]                                   # speichert den Faktor, mit dem multipliziert werden muss, da dieser auch verändert wird
            for n in range(len(calc[0])):                           # zählt die Spalte um die gesamte Spalte zu subtrahieren
                calc[l][n] -= factor * calc[i][n]                   # subtrahiert die aufgelöste Spalte im vielfachen von der aktuellen Spalte
    
    
    """
    bringt die Matrix in die Form:
        w1      1       0       0       0 ...
        w2      0       1       0       0 ...
        w3      0       0       1       0 ...
        .
        .
        .
    """
    
    for i in range(len(calc), -1, -1):                              # Gibt sowohl den Wert der aktuel zu berechnenden Reihe an, als auch, auf Grund der Form der Matrix, die Spalte mit dem zur Berechnung notwendigen Wert
        for j in range(i-1):                                        # Geht die zu berechnenden Spalten der entsprechnden Reihe durch
            for k in range(len(calc[0])):                           # Geht die zu Reihe der zu berechnenden Spalte durch
                calc[j][k] -= calc[i-1][k]*calc[j][i]               # Die Zeilen werden von Unten nach oben subtrahiert um die angegebe Form zu erreichen
    
    return calc