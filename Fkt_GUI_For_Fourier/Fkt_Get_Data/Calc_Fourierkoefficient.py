# -*- coding: utf-8 -*-
"""
Übergribt den Wert des Fourierkoeffizienten bei 
Empfang des genäherten Polynoms (polykoef) der Form:
c0  1   0   0   .   .   .
c1  0   1   0   .   .   .
c2  0   0   1   .   .   .
.   .
.       .
.           .
wobei ci die Faktoren des Polynoms sind mit c0x^0, c1x^1, ...
Aus der Anzahl der reihe wird der Grad des Polynoms bestimmt. Die erste Spalte wird als Information benötigt. 
Der Rest nicht beachtet, weshalb die Reihenfolge der ci relevant ist. 
Außerdem muss gegeben sein die Nummer des Koeffizienten (k), 
ob Koeffizient a oder b gewollt ist (ab)
und die Länge der Periode (p).

Das zu berechnende Integral von 0 bis 24 ergibt sich aus der Summe von den Ableitungen des Polynoms multipliziert mit den trigonometrischen Funktionen in entsprechend hoher Stammfunktion.
"""

import sympy as sp
import math as m

import Fkt_GUI_For_Fourier.Fkt_Get_Data.Fkt_Calc_Fourierkoefficient as fkt

def Calc_Fourierkoefficient(polykoef, k, ab, p):     # Polykoef Matrix, die in der ersten Spalte nur die Koeffizienten eines Polynoms enthält, k ist die Nummer des Fourierkoeffizienten, ab gibt mit 0 Koeffizient a und mit 1 b an, p die Länge der Periode
    koef = 0.0                                  # Definition des aktuel zu berechneden Koeffizienten, der nach und nach berechnet wird
    integralfactor = k * 2* sp.pi / p           # Berechnung des Faktors ohne Potenz, der durch das Integrieren vor die trigonomatrische Funktion kommt. Diese wird anschließend potenziert
    trigonfactor = 2 * sp.pi / p * k            # Berechnung des Faktors, der in die trigonometrische Funktion, vor das x gehört.
    if k == 0:
        if ab == 0:
            koef += fkt.Integral_Poly(polykoef, p)   # Berechnung von a0, ohne weitere Faktoren
        else:
            return 0.0                          # b0 ist immer 0, deshalb keine Rechnung nötig
    else:
        if ab == 0:                                 # ab gibt an ob es sich um den Koeffizienten a oder b handelt, wobei 0 für a und 1 für b steht.
            for i in range(0, len(polykoef), 2):    # Berechnet alle Teile der Summe der Stammfunktion, die mit einem Sinus berechnet werden für einen Koeffizienten a
                polynom = fkt.Poly_For_Integral(polykoef, i)      # bekommt die Koeffizienten der i-ten Ableitung des Polynoms als Array
                koef += m.pow(-1, ((i/2) %2)) * 1/m.pow(integralfactor, i+1) *m.sin(trigonfactor *p) * fkt.Calc_Poly(polynom, p, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem hohen Wert des Integrals
                koef -= m.pow(-1, (i/2) %2) * 1/m.pow(integralfactor, i+1) *m.sin(trigonfactor *0) * fkt.Calc_Poly(polynom, 0, i)       # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem niedrigen Wert des Integrals
            for i in range(1, len(polykoef), 2):    # Berechnet alle Teile der Summe der Stammfunktion, die mit einem Cosinus berechnet werden für einen Koeffizienten a
                polynom = fkt.Poly_For_Integral(polykoef, i)
                koef += m.pow(-1, (i-1) /2 %2) * 1/m.pow(integralfactor, i+1) *m.cos(trigonfactor *p) * fkt.Calc_Poly(polynom, p, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem hohen Wert des Integrals
                koef -= m.pow(-1, (i-1) /2 %2) * 1/m.pow(integralfactor, i+1) *m.cos(trigonfactor *0) * fkt.Calc_Poly(polynom, 0, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem niedrigen Wert des Integrals
        else:
            for i in range(0, len(polykoef), 2):    # Berechnet alle Teile der Summe der Stammfunktion, die mit einem Cosinus berechnet werden für einen Koeffizienten b
                polynom = fkt.Poly_For_Integral(polykoef, i)      # bekommt die Koeffizienten des Polynoms als Array
                koef += m.pow(-1, (i+2) /2 %2) * 1/m.pow(integralfactor, i+1) *m.cos(trigonfactor *p) * fkt.Calc_Poly(polynom, p, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem hohen Wert des Integrals
                koef -= m.pow(-1, (i+2) /2 %2) * 1/m.pow(integralfactor, i+1) *m.cos(trigonfactor *0) * fkt.Calc_Poly(polynom, 0, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem niedrigen Wert des Integrals
            for i in range(1, len(polykoef), 2):    # Berechnet alle Teile der Summe der Stammfunktion, die mit einem Sinus berechnet werden für einen Koeffizienten b
                polynom = fkt.Poly_For_Integral(polykoef, i)
                koef += m.pow(-1, (i-1) /2 %2) * 1/m.pow(integralfactor, i+1) *m.sin(trigonfactor *p) * fkt.Calc_Poly(polynom, p, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem hohen Wert des Integrals
                koef -= m.pow(-1, (i-1) /2 %2) * 1/m.pow(integralfactor, i+1) *m.sin(trigonfactor *0) * fkt.Calc_Poly(polynom, 0, i)     # Berechnet einen Wert der Summe von der Stammfunktion mit eingesetztem niedrigen Wert des Integrals
    koef *= 2 /p                                # Der Vorfaktor des gesamten Koeffizienten
    return koef