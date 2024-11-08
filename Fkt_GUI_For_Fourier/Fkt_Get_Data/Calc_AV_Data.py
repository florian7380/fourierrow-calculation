"""
Berechnung der durchschnittlichen Werte einer Periode (Eines Tages)
"""
import numpy as np

def Calc_AV_Data(n_period, data):
    av_data = np.array([[0.0] * n_period] * 2)      # In der neuen Matrix wird ein Array mit den durchschnittliochen Werten der Leistung gespeichert
    for i in range(n_period):
        for j in range(int(len(data)/n_period)):
            av_data[1][i] += data[i+j*n_period][1]  # addiert alle Werte die zur selben Zeit, an unterschiedlichen Tagen aufgenommen wurden, zusammen
        av_data[1][i] /= len(data)/n_period         # Teilt den Wert durch die Anzahl der eingelesenen Tage
        av_data[0][i] = data[i][0]                  # Nimmt die Zeit für den entsprechenden Wert auf
    return av_data