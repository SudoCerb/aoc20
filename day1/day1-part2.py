import pandas as pd

data = pd.read_csv('../input.txt', header=None)
# print(data.head())

# sumMatrix = data.copy()
# for i in data.index:
#     sumMatrix[i] = None

for i in data.index:
    for j in data.index:
        for k in data.index:
            sumVal = data[0][i] + data[0][j] + data[0][k]

            if sumVal == 2020:
                print("INDICES")
                print(i,j,k)
                print("VALUES")
                print(data[0][i])
                print(data[0][j])
                print(data[0][k])
                print("MULTIPLIED")
                print(data[0][i]*data[0][j]*data[0][k])
