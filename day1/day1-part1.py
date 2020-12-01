import pandas as pd
import sys

data = pd.read_csv('input.txt', header=None)

for i in data.index:
    for j in data.index:
        sumVal = data[0][i] + data[0][j]
        if sumVal == 2020:
            print("", "INDICES", sep='\n')
            print(i, j)
            print("","VALUES", sep='\n')
            print(data[0][i],data[0][j])
            print("","MULTIPLIED", sep='\n')
            print(data[0][i]*data[0][j])
            sys.exit()
