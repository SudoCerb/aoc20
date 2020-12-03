file = open('input.txt','r')
lines = file.readlines()
rf = []  # reference field
for line in lines:
    rf.append(line)

modulo = len(rf[0]) - 1
treeCounter = 0

horizPath = 3
vertPath = 1

lz = 0  # present horizontal location

def getHorizLoc(x):
    if x % modulo == 0 and x != 0:
        return 0
    else:
        return x % modulo

for line in rf:  # currently this increments vertical by 1
    hl = getHorizLoc(lz)
    indicator = ['^' if x == hl else ' ' for x in range(modulo)]
    indicator = ''.join(indicator)
    print(line + indicator)
    print(hl)
    # check if tree
    if line[hl] == '#':
        treeCounter += 1
    # move to next location
    lz += horizPath

print(treeCounter)