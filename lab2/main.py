import pandas as pd
import numpy as np
import math

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

#ustawienie gęstości
density = 950 * 10**-3

#wyliczanie maksimum i minimum
d_min, d_max = get_maximums(d, 0.01 / 1000)
h_min, h_max = get_maximums(h, 1 / 1000)
t_min, t_max = get_maximums(t, 0.01, 0.5)


#wyliczenie średnich
d = np.mean(d)
h = np.mean(h)
t = np.mean(t)


u_Ft_d = 0.5 *np.abs(3 * np.pi * density * d_max * h / t - 3 * np.pi * density * d_min * h / t)
u_Ft_h = 0.5 *np.abs(3 * np.pi * density * d * h_max / t - 3 * np.pi * density * d * h_min / t)
u_Ft_t = 0.5 *np.abs(3 * np.pi * density * d * h / t_max - 3 * np.pi * density * d * h / t_min)


u_Ft = np.sqrt(u_Ft_d ** 2 + u_Ft_h ** 2 + u_Ft_t ** 2)

Ft = 3 * np.pi * density * d * h / t

print(f"F_t = {Ft} N +- {u_Ft}")