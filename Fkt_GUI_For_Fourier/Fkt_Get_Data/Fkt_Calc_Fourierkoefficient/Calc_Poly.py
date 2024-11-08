"""
Hier wird ein Polynom und dessen Ableitungen berechnet.
Benötigt wird:
Ein Array der Form: [a0 a1 a2 ... ] für die Koeffizienten des Polynoms (koef), (Die Arraygröße legt den Grad des Polynoms der Grundfunktion fest)
Den x-Wert, für den das Polynom berechnet werden soll (x)
die Nummer der Ableitung "die n-te Ableitung" (n)
Der Grad der Ableitung wird benötigt um die richtigen Exponenten bei gleich bleibender Arraygröße zu finden.
"""

def Calc_Poly(koef, x, n):   # koef ist ein Array mit allen Koeffizienten des Polynoms in der Form [a0 a1 a2 ... ], x der x-Wert für den das Polynom berechnet werden soll, n gibt die Ableitung an.
    y = 0.0
    for i, e in enumerate(koef):
        if i >= n:
            y += e * x**(i-n)
    return y