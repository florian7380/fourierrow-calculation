"""
Zählt die Anzahl Werte in einer Periode
"""
    
def Number_Of_Values_In_Period(data):    
    for i in range(1, len(data)):
        if data[0][0] == data[i][0]:                # Zählt die Anzahl der Werte, bis die Zeiteinheit erneut auftritt und damit die Anzahl der Werte für einen Tag
            return i