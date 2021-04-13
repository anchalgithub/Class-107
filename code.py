#finding out each class's assement data
import csv
import pandas as pd
import plotly.graph_objects as go
 
#reading the file and then grouping and calculating each level's attempt's mean.
df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

#displaying it in a horizontal bar graph
fig = go.Figure(go.Bar(
x=df.groupby("level")["attempt"].mean(),
y=['level 1', 'level 2','level 3', 'level 4'],
orientation='h',

))
fig.show()