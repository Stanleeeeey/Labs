import pandas as pd
import numpy as np

from lib import get_maximums

# ścieżka do danych
data_path = "data/"

#otworzenie plików
d_file = pd.read_csv( data_path + "d.csv")
h_file = pd.read_csv( data_path + "h.csv")
t_file = pd.read_csv( data_path + "t.csv")



#wczytanie danych i zamiana na standartowe jednostki układu SI
d = d_file["d[mm]"].to_numpy().astype(np.float64) / 1000
h = h_file["h[mm]"].to_numpy().astype(np.float64) / 1000
t = t_file["t[s]"].to_numpy().astype(np.float64)

#wyliczanie maksimum i minimum
d_min, d_max = get_maximums(d, 0.01 / 1000)
h_min, h_max = get_maximums(h, 1 / 1000)
t_min, t_max = get_maximums(t, 0.01, 0.5)

