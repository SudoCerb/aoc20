import math
file = open('input.txt','r')
lines = file.read().splitlines()
maxSeatId = 0
for line in lines:
    upperRow = 128 - 1
    lowerRow = 0
    upperCol = 8 - 1
    lowerCol = 0
    for char in line:
        if char == 'F':
            upperRow = math.floor(upperRow - (upperRow - lowerRow) / 2)
        elif char == 'B':
            lowerRow = math.ceil(lowerRow + (upperRow - lowerRow) / 2)
        elif char == 'L':
            upperCol = math.floor(upperCol - (upperCol - lowerCol) / 2)
        elif char == 'R':
            lowerCol = math.ceil(lowerCol + (upperCol - lowerCol) / 2)
    seatId = upperRow * 8 + upperCol
    if seatId > maxSeatId:
        maxSeatId = seatId
    print('LINE:', line, 'ROW:', upperRow, 'COL:', upperCol, 'SEAT_ID:', seatId)
print('MAX_SEAT_ID: ',maxSeatId)