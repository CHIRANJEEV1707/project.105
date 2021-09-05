from os import stat
import pandas as pd
import statistics
import csv

df=pd.read_csv(r"C:\Users\Chiranjeev\OneDrive\Desktop\project105\SOCR-HeightWeight.csv")

h=df["Weight"]
n=len(h)

mode=statistics.mode(h)
median=statistics.median(h)
mean=statistics.mean(h)

print("median=",median)
print("mean=",mean)
print("mode",mode)