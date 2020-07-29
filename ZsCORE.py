import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df= pd.read_csv("School1.csv")
data = df["Math_score"].to_list()
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

mean_list=[]
for i in range(0, 1000):
    setOfMeans= randomSetOfMean(100)
    mean_list.append(setOfMeans)
mean= statistics.mean(mean_list)
print("Mean of the Sampling Distribution: ", mean)

standDev= statistics.stdev(mean_list)
print("Standard Deviation of the Sampling Distribution: ", standDev)

i_std_start, i_std_end = mean - standDev, mean + standDev
ii_std_start, ii_std_end = mean - (standDev*2), mean + (standDev*2)
iii_std_start, iii_std_end = mean - (standDev*3), mean + (standDev*3)

print("Std_1: ", i_std_start, i_std_end)
print("Std_2: ", ii_std_start, ii_std_end)
print("Std_3: ", iii_std_start, iii_std_end)
