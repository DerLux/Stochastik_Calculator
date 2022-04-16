# inputs
import statistics as stat
import numpy as np
import pandas as pd

list0, list1, list2, list3 = {}, {}, {}, {}

select = int(input("\nBitte auswählen, in welche Liste(0-3) die Eingabe gespeichert werden soll:"))
if select == 0:  # List0 für 'Beschreibende Statistik'
    list0 = list(map(int, input("\nBitte Urliste eingeben:").split()))
if select == 1:  # List1
    list1 = list(map(int, input("\nBitte Urliste eingeben:").split()))
if select == 2:  # List2
    list2 = list(map(int, input("\nBitte Urliste eingeben:").split()))
if select == 3:  # List3
    list3 = list(map(int, input("\nBitte Urliste eingeben:").split()))

# List0 wir ausgeführt
if select == 0:

    absolut = pd.Series(list0).value_counts()

    print("\nAbsolute Wahrscheinlichkeit:\n", absolut)
    print("\nRelative Wahrscheinlichkeit:\n", absolut/len(list0))

    print("\nModalwert(e):", stat.multimode(list0))
    print("Median = ", np.quantile(list0, 0.5))
    print("arithmetisches Mittel = ", np.mean(list0))
    print("Standartabweichung = ", np.std(list0, ddof=1))
    print("Interquartilsabstand: ", np.percentile(list0, 75) - np.percentile(list0, 25))
    print("Spannweite = ", max(list0) - min(list0))

    print("\n25% Quantil =", np.quantile(list0, 0.25, method="averaged_inverted_cdf"))
    print("50% Quantil =", np.quantile(list0, 0.5, method="averaged_inverted_cdf"))
    print("75% Quantil =", np.quantile(list0, 0.75, method="averaged_inverted_cdf"))

    count = int(input("\nAnzahl zusätzlicher Werte: "))
    if count > 0:
        quant = list(map(float, input("Bitte Wert zwischen [0,1] eingeben: ").split()))
        print("\n")
        for x in range(0, count):
            print("{}% Quantil =".format(quant[x]), np.quantile(list0, quant[x], method="averaged_inverted_cdf"))
