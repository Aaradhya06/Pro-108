import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("c:/Aaradhya/Projects/Project-108/data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],)
fig.show()