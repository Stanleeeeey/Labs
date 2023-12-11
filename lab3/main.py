import pandas as pd
import numpy as np

data_path = "data/"

delta_l_file = pd.read_csv( data_path + "delta_L.csv")
I_file       = pd.read_csv( data_path + "I.csv")
T_file       = pd.read_csv( data_path + "T.csv")
U_file       = pd.read_csv( data_path + "U.csv")

delta_l = delta_l_file["delta_L[mm]"].to_numpy().astype(np.float64) / 1000
I       = I_file["I[A]"].to_numpy().astype(np.float64)
T       = T_file["T[C]"].to_numpy().astype(np.float64)
U       = U_file["U[V]"].to_numpy().astype(np.float64)
