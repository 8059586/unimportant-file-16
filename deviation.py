import csv

with open("class1.csv",newline="")as a:
    reader = csv.reader(a)
    data = list(reader)

data.pop(0)
newdata = []
for i in range(0,len(data)):
    num = data[i][1]
    newdata.append(float(num))

sum = 0
for g in newdata:
    sum+=g
mean = sum/len(newdata)
print(mean)

import pandas as pd
import plotly.express as px
df = pd.read_csv("class1.csv")
graph = px.scatter(df,x="Student Number",y="Marks")
graph.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=len(newdata))])
graph.show()

squarelist=[]
data = df["Marks"]
for i in data:
    x = int(i)-mean
    x = x**2
    squarelist.append(x)

sum2 = 0
for g in squarelist:
    sum2+=g

somename = sum2/(len(data)-1)

import math
deviation = math.sqrt(somename)
print(deviation)