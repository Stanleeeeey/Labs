import pandas as pd
import numpy as np
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

