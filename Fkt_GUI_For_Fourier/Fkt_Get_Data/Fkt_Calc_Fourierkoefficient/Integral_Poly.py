"""
Berechnet den Wert des Integrals eines Polynoms von 0 bis x. Übergeben werden:
Das Polynom als Matrix bei der in der ersten Spalte die Faktoren des Polynoms stehen. Alles andere wird nicht ausgelesen.
Die matrix hat die Form: (polykoef) 
c0  1   0   0   .   .   .
c1  0   1   0   .   .   .
c2  0   0   1   .   .   .
.   .
.       .
.           .
und das Ende des Integrals (x)
"""
   
def Integral_Poly(polykoef, x):
    koef = 0.0
    for i, e in enumerate(polykoef):
        koef += e[0]/(i+1)*x**(i+1)         # e[0] sind die einzelnen Faktoren des Polynoms, die durch den Exponenten geteilt werden um die Stammfunktion nachzubilden. x^(i+1) bewirkt den erhöhten Exponenten durch die Stammfunktion.
    return koef