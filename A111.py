import csv
import statistics
import random
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print(population_mean)

def random_mean():
    dataset = []
    for i in range(0,30):
        rx = random.randint(0,len(data)-1)
        value = data[rx]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mlist = []
for i in range(0,100):
    mean_set = random_mean()
    mlist.append(mean_set)


means = statistics.mean(mlist)
print(means)

std = statistics.stdev(mlist)

fig = ff.create_distplot([mlist],["reading_time"],show_hist = False)
fig.show()

h1start,h1end = means-std,means+std
h2start,h2end = means-(2*std),means+(2*std)
h3start,h3end = means-(3*std),means+(3*std)

df = pd.read_csv("sample.csv")
data = df["reading_time"].tolist()

sample_mean = statistics.mean(data)
print(sample_mean)

fig = ff.create_distplot([mlist], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[means, means], y=[0, 1.4], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sample_mean,sample_mean], y=[0, 1.4], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[h1end, h1end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[h2end,h2end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[h3end,h3end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

