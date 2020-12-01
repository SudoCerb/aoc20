import pandas as pd
import sys

data = pd.read_csv('input.txt', header=None)

for i in data.index:
    for j in data.index:
        for k in data.index:
            sumVal = data[0][i] + data[0][j] + data[0][k]

            if sumVal == 2020:
                print("","INDICES", sep='\n')
                print(i,j,k)
                print("","VALUES", sep='\n')
                print(data[0][i],data[0][j],data[0][k])
                print("","MULTIPLIED", sep='\n')
                print(data[0][i]*data[0][j]*data[0][k])
                sys.exit()
