"""
Berechnung der Fakultät (n!)
Übergeben wird ein Integer (x)
gibt None zurück, wenn x negativ ist
"""

def Faculty(x):             # Berechnung der Fakultät der Zahl x
    y = 1                   # Zahl die weiter multipliziert wird
    if x >= 0:              # Prüfen auf positive Zahl
        for i in range(1, x+1):
            y *= i          # Die Multiplikatoren werden hinzu berechnet
        return y
    else:
        return