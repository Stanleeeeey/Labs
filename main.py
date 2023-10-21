import pandas as pd
import numpy as np
import math

from lib import *

data_path = "data/"

d_file = pd.read_csv( data_path + "d.csv")
D_file = pd.read_csv( data_path + "capital_d.csv")
m_file = pd.read_csv( data_path + "m.csv")
T_file = pd.read_csv(data_path  + "T.csv")

d = d_file["d[mm]"].to_numpy().astype(np.float64) / 1000
D = D_file["D[mm]"].to_numpy().astype(np.float64) / 1000
m = m_file["m[g]"].to_numpy().astype(np.float64) / 1000
T = T_file["T[s]"].to_numpy().astype(np.float64) / 50

min_d, max_d = get_maximums(d, 0.02 / 1000)
min_D, max_D = get_maximums(D, 0.02 / 1000)
min_m, max_m = get_maximums(m, 0.1 / 1000)
min_T, max_T = get_maximums(T, 0.01, 0.1)


d = np.mean(d)
D = np.mean(D)
m = np.mean(m)
T = np.mean(T)

u_TI = 0.5* np.abs((max_T**2 * m * GRAVITY * d / 2) / (4*math.pi**2) - (min_T**2 * m * GRAVITY * d / 2) / (4*math.pi**2))
u_mI = 0.5* np.abs((T**2 * max_m * GRAVITY * d / 2) / (4*math.pi**2) - (T**2 * min_m * GRAVITY * d / 2) / (4*math.pi**2))
u_dI = 0.5* np.abs((T**2 * m * GRAVITY * max_d / 2) / (4*math.pi**2) - (T**2 * m * GRAVITY * min_d / 2) / (4*math.pi**2))

uI = np.sqrt( u_TI**2  +  u_mI**2 +  u_dI**2)


print(uI)