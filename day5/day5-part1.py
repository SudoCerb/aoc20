import math
file = open('input.txt','r')
lines = file.read().splitlines()
maxSeatId = 0
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
    if upperRow * 8 + upperCol > maxSeatId:
        maxSeatId = upperRow * 8 + upperCol
print('MAX_SEAT_ID: ',maxSeatId)