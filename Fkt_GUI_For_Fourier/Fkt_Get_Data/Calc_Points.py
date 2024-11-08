# -*- coding: utf-8 -*-
"""
Berechnung einzelner durchschnittlicher Punkte für die Berechnung des Polynoms
"""

import numpy as np

def Calc_Points(n_period, var, av_data):
    c_points = int(n_period/var)                    # Berechnet die Anzahl der zusammen zu rechnenden Werte um einen durchnittlichen Punkt zu finden, durch dne das Polynom laufen muss
    add_val = n_period % var                        # Da die Zahl im Normalfall nicht aufgeht muss der Rest beachtet werden und auf einige Punkte aufgeteilt werden 
    points = np.array([[None] * (var+2)] * 2)       # Points ist die Matrix in der die x- und y-Werte der punkte für das Polynom bestimmt werden. Es werden 2 Punkte mehr gespeichert um den Start und Endwert festzustellen und eine Periode zu gewährleisten, die nicht unbedingt in den Ursprungsdaten vorhanden ist. 
    
    for i in range(var):
        if i < add_val:                             # Prüft ob schon ein zusätzlicher Wert hinzugenommen werden muss, um den oben bestimmten Rest auch auf die Punkte zu verteilen
            start_of_c_points = i*(c_points+1)      # Berechent den Startwert, der zur Berechnung des durchschnittlichen Punktes, mit zusätzlichem Wert des Rests gebraucht wird
            end_of_c_points = (i+1)*(c_points+1)    # Berechent den Endwert, der zur Berechnung des durchschnittlichen Punktes, mit zusätzlichem Wert des Rests gebraucht wird
        else:
            start_of_c_points = i*c_points + add_val      # Berechent den Startwert, der zur Berechnung des durchschnittlichen Punktes gebraucht wird
            end_of_c_points = (i+1)*c_points + add_val    # Berechent den Endwert, der zur Berechnung des durchschnittlichen Punktes gebraucht wird
        points[0][i+1] = sum(av_data[0][start_of_c_points:end_of_c_points])/(end_of_c_points-start_of_c_points)   # Berechnet den Durchschnittswert der Zeiten
        points[1][i+1] = sum(av_data[1][start_of_c_points:end_of_c_points])/(end_of_c_points-start_of_c_points)   # Berechent den Durchschnittswert der Leistungen
    
    points[0][0] = av_data[0][0]                                                    #Die 4 Zeilen setzen den ersten und letzten Punkt gleich und durchschnittlich um eine geschlossene Periode vorzutäuschen
    points[1][0] = (av_data[1][0]+av_data[1][len(av_data[1])-1])/2
    points[0][len(points[0])-1] = av_data[0][len(av_data[0])-1]+0.01
    points[1][len(points[0])-1] = (av_data[1][0]+av_data[1][len(av_data[1])-1])/2
    
    return points
    