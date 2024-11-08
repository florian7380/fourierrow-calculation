"""
Umrechnung der Zeit der Form hh:mm in die Form x.xx h
"""

def Change_Time_Format(data):
    time_as_string = [None] * 2                 # Die Zeit ist in h:min gegeben und wird im Folgenden in x,xx Stunden umgerechnet
    for i, e in enumerate(data):
        data[i][1] = data[i][1].replace(".", "")    # Die Zahlen haben eine deutsche Schreibweise mit "." als Trenner nach jeweils 3 Stellen, die entfernt werden
        data[i][1] = data[i][1].replace(",", ".")   # und einem "," als Trenner zwischen 1ser und Zehntel, das in einen "." geändert wird
        data[i][1] = float(data[i][1])              # Nun wird die so veränderte Zahl als float eingelesen
        time_as_string = data[i][0].split(":")      # Die Zeit in der Form hh:minmin am ":" getrennt
        data[i][0] = float(time_as_string[0]) + float(time_as_string[1])/60  # Berechnung der Stunden mit der Umrechnung der Minuten in 0,... Stunden
    return data