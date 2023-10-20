import pandas as pd

data_path = "data/"

d_file = pd.read_csv( data_path + "d.csv")
D_file = pd.read_csv( data_path + "capital_d.csv")
m_file = pd.read_csv( data_path + "m.csv")
T_file = pd.read_csv(data_path  + "T.csv")


print(d_file["d[mm]"])
print(D_file["D[mm]"])
print(m_file["m[g]"])
print(T_file["T[s]"])