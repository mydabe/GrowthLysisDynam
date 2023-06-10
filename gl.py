import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importing optical density data taken from Tecan K Microplate Reader (Excel File)
df = pd.read_excel("20230126_keiogfp_cm25_37CM9CAvwr_carb25_amx5_screening.xlsx", sheet_name = "Sheet3")
df.index
df2 = pd.read_excel("20230126_keiogfp_cm25_37CM9CAvwr_carb25_amx5_screening.xlsx", sheet_name = "Sheet4")
df2.index
dataRange = np.arange(35, 416)
"""
Initializing arrays of desirable data from the Excel File (timespan, optical density, and an array that references 
the two antibiotics tested: carbenicillin and amoxicillin (carbencillin data appeared on odd columns, while amoxicillin on even columns).
"""
tspa = list(np.array(df.iloc[33, 1:26]))
tspan = np.array(tspa) / 3600
tspan1 = list(np.array(df.iloc[33, 1:81]))
alternatingRange = np.arange(35, 416, 2)
t = list(np.arange(0, 17, 0.162))
"""
This function plots the optical density data over the time in which the plate reader was collecting data (~16 hrs). If the parameter ln is
set to True, the natural log of the optical density data will be displayed.
"""
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
"""
The growth function below takes in index array which refers to the column of data to be analyzed. The slope of the linear 
trend in the initial four hour period is returned as an approximate growth rate for that specific strain 
(whether it be carbenicillin or amoxicillin). 
"""
def Growth(index) :
    lnOD = []
    OD = list(np.array(df.iloc[index, 1:26]))
    for i in OD :
        lnOD.append(np.log(i))
    n = lnOD.index(max(lnOD))
    GR = (max(lnOD) - lnOD[n-1]) / (tspan[n] - tspan[0])
    return GR
"""
The lysis function below, similar to the growth function above, takes in column of data "index" as a parameter. The growth function is then 
called on the same column of data, and is used to calculate the lysis rate as approximated in "Robust, linear correlations between growth
rates and beta-lactam-mediated lysis rates" (Anna Lee et al. 2018).
"""

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

Growth1 = list([])
Lysis1 = list([])

"""
This loop creates the Growth vs. Lysis plot. Calculates the growth and lysis rates according to the functions above, and plots the data.
"""
for i in alternatingRange :
    Growth1.append(Growth(i))
    Lysis1.append(Lysis(i))
    plt.grid(True)
    plt.scatter(Growth1, Lysis1)
    plt.xlabel("Growth Rate (ln(OD600)/hr)")
    plt.ylabel("Lysis Rate (ln(OD600)/hr)")

#Plotting the line of best fit for the data    
x, y = np.polyfit(Growth1, Lysis1, 1)
plt.plot(Growth1, x*np.array(Growth1) + y)
plt.show()
