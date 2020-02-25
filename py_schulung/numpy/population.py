import pandas as pd

data = pd.read_csv("https://python-course.eu/material/data1/germany/"
                     "bevoelkerung_bundeslaender.txt", sep = "\t")

print(data)

print(data.loc[data.bevoelkerung > 10000])
