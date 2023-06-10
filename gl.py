import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial
import math
from sympy import *
df = pd.read_excel("20230126_keiogfp_cm25_37CM9CAvwr_carb25_amx5_screening.xlsx", sheet_name = "Sheet3")
df.index
df2 = pd.read_excel("20230126_keiogfp_cm25_37CM9CAvwr_carb25_amx5_screening.xlsx", sheet_name = "Sheet4")
df2.index
dataRange = np.arange(35, 416)

tspa = list(np.array(df.iloc[33, 1:26]))
tspan = np.array(tspa) / 3600
tspan1 = list(np.array(df.iloc[33, 1:81]))
alternatingRange = np.arange(35, 416, 2)
Growth1 = list([])
Lysis1 = list([])
#for i in tspan1 :
    #tspan.append(i)
t = list(np.arange(0, 17, 0.162))
def Plotter(index, ln=False) :
    lnOD = []
    OD = list(np.array(df.iloc[index, 1:26]))
    Odp2 = list(np.array(df2.iloc[index, 1:81]))    
    for j in Odp2 :
        OD.append(j)
    if ln==True :
        for i in OD :
            lnOD.append(np.log(i))
    plt.grid(True)
    if ln==True :
        plt.plot(t, lnOD, "k-")
        plt.title("ln(OD600) over Time (s)")
        plt.xlabel("Time (s)")
        plt.ylabel("ln(OD600)")
    else :
        plt.plot(t, OD, "k-")
        plt.title("OD600 over Time (s)")
        plt.xlabel("Time (s)")
        plt.ylabel("OD600")
    return True

#Plotter(35)
def Growth(index) :
    lnOD = []
    OD = list(np.array(df.iloc[index, 1:26]))
    #Odp2 = list(np.array(df2.iloc[index, 1:14]))    
    #for j in Odp2 :
        #OD.append(j)
    for i in OD :
        lnOD.append(np.log(i))
    n = lnOD.index(max(lnOD))
    GR = (max(lnOD) - lnOD[n-1]) / (tspan[n] - tspan[0])
    return GR

def Lysis(index) :
    lnOD = []
    OD = list(np.array(df.iloc[index, 1:26]))
    Odp2 = list(np.array(df2.iloc[index, 1:81]))    
    for j in Odp2 :
        OD.append(j)
    for i in OD :
        lnOD.append(np.log(i))
    GR = Growth(index)
    n =Odp2.index(min(Odp2))
    L = GR - ((min(Odp2) - Odp2[n-1]) / (t[n]- t[n-1]))
    return L

Lysis(35)#
for i in alternatingRange :
    Growth1.append(Growth(i))
    Lysis1.append(Lysis(i))
    plt.grid(True)
    plt.scatter(Growth1, Lysis1)
    plt.xlabel("Growth Rate (ln(OD600)/hr)")
    plt.ylabel("Lysis Rate (ln(OD600)/hr)")
x, y = np.polyfit(Growth1, Lysis1, 1)



plt.plot(Growth1, x*np.array(Growth1) + y)
plt.show()
print(alternatingRange[58])
#print(Growth1)
#print(Lysis1)
print(Growth1.index(0.03440055661088445))
