import math
file = open('input.txt','r')
lines = file.read().splitlines()
maxSeatId, seatIds = 0, []
for line in lines:
    upperRow, lowerRow, upperCol, lowerCol = 128 - 1, 0, 8 - 1, 0
    for char in line:
        if char == 'F':
            upperRow = math.floor(upperRow - (upperRow - lowerRow) / 2)
        elif char == 'B':
            lowerRow = math.ceil(lowerRow + (upperRow - lowerRow) / 2)
        elif char == 'L':
            upperCol = math.floor(upperCol - (upperCol - lowerCol) / 2)
        elif char == 'R':
            lowerCol = math.ceil(lowerCol + (upperCol - lowerCol) / 2)
    seatIds.append(upperRow * 8 + upperCol)
    if seatIds[-1] > maxSeatId:
        maxSeatId = seatIds[-1]
seatIds.sort()
for i in range(len(seatIds)):
    if seatIds[i + 1] - seatIds[i] != 1:
        print('YOUR SEAT:', seatIds[i] + 1)
        break
