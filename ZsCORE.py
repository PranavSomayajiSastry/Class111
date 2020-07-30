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

print("Std_1: ", i_std_start,"and", i_std_end)
print("Std_2: ", ii_std_start,"and", ii_std_end)
print("Std_3: ", iii_std_start,"and", iii_std_end)


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].to_list()
meanOfSamp_1= statistics.mean(data)
print("The Mean of the Sample 1: ", meanOfSamp_1)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17],mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSamp_1, meanOfSamp_1], y=[0, 0.17],mode="lines", name="Mean of Student who had Math Labs"))
fig.add_trace(go.Scatter(x=[i_std_end, i_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 1 END"))
fig.add_trace(go.Scatter(x=[ii_std_end, ii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 2 END"))
fig.add_trace(go.Scatter(x=[iii_std_end, iii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 3 END"))

fig.show()



df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].to_list()
meanOfSamp_2= statistics.mean(data)
print("The Mean of the Sample 2: ", meanOfSamp_2)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17],mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSamp_2, meanOfSamp_2], y=[0, 0.17],mode="lines", name="Mean of Students who used Application"))
fig.add_trace(go.Scatter(x=[i_std_end, i_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 1 END"))
fig.add_trace(go.Scatter(x=[ii_std_end, ii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 2 END"))
fig.add_trace(go.Scatter(x=[iii_std_end, iii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 3 END"))

fig.show()



df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].to_list()
meanOfSamp_3= statistics.mean(data)
print("The Mean of the Sample 3: ", meanOfSamp_3)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17],mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSamp_3, meanOfSamp_3], y=[0, 0.17],mode="lines", name="Mean of Students who Math Registers"))
fig.add_trace(go.Scatter(x=[i_std_end, i_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 1 END"))
fig.add_trace(go.Scatter(x=[ii_std_end, ii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 2 END"))
fig.add_trace(go.Scatter(x=[iii_std_end, iii_std_end], y=[0, 0.17],mode="lines", name="Standard Deviation 3 END"))

fig.show()

z_score= (meanOfSamp_1-mean )/standDev
print("The Z-Score of Sample 1:", z_score)

z_score2= (meanOfSamp_2-mean)/standDev
print("The Z-Score of Sample 2:", z_score2)

z_score3= (meanOfSamp_3-mean )/standDev
print("The Z-Score of Sample 3:", z_score3)