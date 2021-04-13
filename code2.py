#finding out each student's assement data
import csv
import pandas as pd
import plotly.graph_objects as go
 
#reading the file and then grouping and calculating each level's attempt's mean.
df = pd.read_csv("data.csv")
student_df=df.loc[df['student_id']=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

#displaying it in a horizontal bar graph
fig = go.Figure(go.Bar(
x=student_df.groupby("level")["attempt"].mean(),
y=['level 1', 'level 2','level 3', 'level 4'],
orientation='h',

))
fig.show()