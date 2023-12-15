import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from lib import ub

data_path = "data/"

delta_l_file = pd.read_csv( data_path + "delta_L.csv")
I_file       = pd.read_csv( data_path + "I.csv")
T_file       = pd.read_csv( data_path + "T.csv")
U_file       = pd.read_csv( data_path + "U.csv")

T_0 = 23.3

delta_l = delta_l_file["delta_L[mm]"].to_numpy().astype(np.float64)[1:] / 1000
I       = I_file["I[A]"].to_numpy().astype(np.float64)[1:]
T       = T_file["T[C]"].to_numpy().astype(np.float64)[1:]
U       = U_file["U[V]"].to_numpy().astype(np.float64)[1:]


L_mean = np.mean(delta_l)
I_mean = np.mean(I)
T_mean = np.mean(T)
U_mean = np.mean(U)

T_precision = T*0.05*0.01 + 0.5 #K
U_precision = U*0.01 + 2*0.1 #V
I_precision = U*2*0.01 + 2*0.01 #A
L_precision = 0.01 #mm

u_T = [ub(t) for t in T_precision]
u_U = [ub(u) for u in U_precision]
u_I = [ub(i) for i in I_precision]
u_L = [ub(L_precision) for i in delta_l]

L_0 = 0.905
u_L_0 = 0.004

L_min, L_max = delta_l - u_L,delta_l+u_L 
U_min, U_max = U - u_U      ,U+u_U
I_min, I_max = I - u_I      ,I+u_I 
T_min, T_max = T - u_T      ,T+u_T  
L_0_min, L_0_max = L_0 - u_L_0, L_0 + u_L_0


u_alpha_L = 0.5 *np.abs(L_min / (L_0 * (T-T_0)) - L_max / (L_0 * (T-T_0)))
u_alpha_L_0 = 0.5 *np.abs(delta_l / (L_0_max * (T-T_0)) - delta_l / (L_0_min * (T-T_0)))
u_alpha_T = 0.5 *np.abs(delta_l / (L_0 * (T_max-T_0)) - delta_l / (L_0 * (T_min-T_0)))


u_alpha = np.sqrt(u_alpha_L**2 + u_alpha_L_0**2 + u_alpha_T**2)

alpha = delta_l / (L_0 * (T-T_0))
print(f"alpha = {alpha} +- {u_alpha}")

u_L_L_by_L_0 = 0.5 *np.abs(L_max/L_0 - L_min/L_0)
u_L_0_L_by_L_0 = 0.5 *np.abs(delta_l/L_0_max - delta_l/L_0_min)

u_L_by_L_0 = np.sqrt(u_L_L_by_L_0**2 + u_L_0_L_by_L_0**2)
print(u_T)
plt.errorbar(y= delta_l/L_0, x=T-T_0, yerr=u_L_by_L_0, xerr=u_T ,fmt='o', capsize=5, markersize = 0, label='Dane z błędami')
plt.axis('equal')
plt.xlim(0)  
plt.ylim(0) 

coefficients = np.polyfit(delta_l/L_0, T-T_0, 1)
polynomial = np.poly1d(coefficients)

x_reg = np.linspace(0, 150, 1000) 

plt.plot(coefficients[0]*x_reg + coefficients[1], x_reg)
plt.show()