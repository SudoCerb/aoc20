import pandas as pd

data = pd.read_csv('../input.txt', header=None)
# print(data.head())

# sumMatrix = data.copy()
# for i in data.index:
#     sumMatrix[i] = None

for i in data.index:
    for j in data.index:
        sumVal = data[0][i] + data[0][j]
        # sumMatrix.iloc[i,j] = data[0][i] + data[0][j]
        if sumVal == 2020:
            print(i,j)
            print("VALUES")
            print(data[0][i])
            print(data[0][j])
            print("MULTIPLIED")
            print(data[0][i]*data[0][j])
