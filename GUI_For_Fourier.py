"""
Dies ist die Oberfläche zur Darstellung der Ergebnisse der Fourierreihe und dient nur der Überprüfung der Berechnungen.
Hier werden die Anzahl der zusätzlichen Puntke für das Polynom, sowie die Anzahl der Fourierkoeffizienten, die berechnet werden sollen, aufgenommen.
Die Werte werden weiter verarbeitet und dann in einem Plot angezeigt. 
"""
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import webbrowser

import Fkt_GUI_For_Fourier as fkt

def Button_Draw(var, koef, link):
    ax.clear()
    values = fkt.Get_Data(var, koef, link)                                                      # Liest den Grad des Polynoms + 2 aus und die Anzahl der zu bildenden Fourierkoeffizienten. Bekommt die Werte cer Durchschnittsberechnung [0], des Polynoms [1] und der Fourierkoeffizienten [2]
    values = fkt.Get_Plot_Values(values)                                                        # Bekommt die y-Werte zu allen x-Werten 
    labels = ["Time in h", "Durchschnittswerte", "Polynom", "Fourierreihe"]                     # Namen für die Beschriftung der Graphen
    for i in range(1, len(values)):
        ax.plot(values[0], values[i], label=labels[i])                                          # Zeichnen der Graohen 
    ax.legend()                                                                                 # Anfügen der Beschriftung der Graphen
        
    canvas.draw()                                                                               # Graphen in den PlOt einfügen
    
def callback(url):
    webbrowser.open_new(url)                # Öffnet einen Browser mit übergebener URL
    

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Näherung durch eine Fourierreihe")
    window.geometry("1000x700")
    
    file_frame = ttk.Frame(master=window)                                   # Frame für den Text der Abfrage des Links zu der CSV-Datei
    file_text1 = tk.Label(file_frame, text = "Von ")                        # Erster Teil des Texts
    link = tk.Label(file_frame, text="hier", fg="blue", cursor="hand2")     # Anklickbarer Text, der dann auf die Webseite führt, auf der die CSV-Dateien heruntergeladen werden können
    link.bind("<Button-1>", lambda e: callback("https://www.smard.de/home/marktdaten?marketDataAttributes=%7B%22resolution%22:%22quarterhour%22,%22from%22:1694124000000,%22to%22:1694383199999,%22moduleIds%22:%5B5000410%5D,%22selectedCategory%22:5,%22activeChart%22:false,%22style%22:%22color%22,%22categoriesModuleOrder%22:%7B%7D,%22region%22:%22DE%22%7D"))   # Link der Webseite und die Verlinkung der entsprechenden Funktion
    file_text2 = tk.Label(file_frame, text=" eine CSV-Datei unter \"mehr\" herunterladen und den Link zur Datei auf dem PC einfügen: ") # zweiter Teil des Texts
    file_text1.pack(side='left')
    link.pack(side='left')
    file_text2.pack(side='left')
    file_frame.pack()
    
    entry_file_frame = ttk.Frame(master=window)                                 # Frame für die Eingabe des Links zu der CSV-Datei
    entry_file = ttk.Entry(entry_file_frame, width=100)
    entry_file.insert(0, r"Bsp.: C:\Users\Name\Documents\Name_der_Tabelle")     # Einsatz eines Beispielpfads
    entry_file.pack(padx=20, pady=10)
    entry_file_frame.pack()
    
    
    poly_frame = ttk.Frame(master = window)                                                         # Bildet den Frame für die Benutzerabfrage fur die Anzahl zusätzlicher Punkte
    points_poly = tk.Label(poly_frame, text="Anzahl der zusätzlichen Punkte für die Näherung des Polynoms (max. 15 empfohlen): ")        # Erklärung, was eingegeben werden soll
    entry_poly = ttk.Entry(poly_frame, width=5)                                                     # Feld für den Eintrag
    points_poly.pack(side = 'left', padx = 56)                                                      # Platzierung innerhalb des Frames
    entry_poly.pack(side = 'right')
    poly_frame.pack(pady = 10)
    
    koef_frame = ttk.Frame(master = window)                                                         # Bildet den Frame für die Benutzerabfrage für die Anzahl der Fourierkoeffizienten
    koef_fourier = tk.Label(koef_frame, text="Anzahl der Fourierkoeffizienten: ")                   # Erklärung, was eingegeben werden soll
    entry_koef = ttk.Entry(koef_frame, width=5)                                                     # Feld für den Eintrag
    koef_fourier.pack(side = 'left', padx = 197)                                                    # Platzierung innerhalb des Frames
    entry_koef.pack(side = 'right')
    koef_frame.pack()                                                                               # Beim Packen Abstand zu anderen Frames eingefügt
    
    button = ttk.Button(window, text="Berechnen", command = lambda: Button_Draw(int(entry_poly.get()), int(entry_koef.get()), str(entry_file.get())))                   # Start der Berechnung durch die Button_draw Funktion
    button.pack(pady = 10)
    
    fig, ax = plt.subplots(figsize=(12,6))
    
    plot_frame = ttk.Frame(master = window)                                                         # Frame für den Linegraph
    canvas = FigureCanvasTkAgg(fig, master = plot_frame)                                            # Grundlage für den Graphen
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(canvas, plot_frame, pack_toolbar = False)                        # Toolbar um zu Zoomen etc.
    toolbar.update()
    toolbar.pack()
    
    plot_frame.pack(pady = 10)
    
    
    window.mainloop()