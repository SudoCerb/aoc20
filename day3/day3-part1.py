file = open('sample_input.txt','r')
lines = file.readlines()
rf = []  # reference field
for line in lines:
    rf.append(line)

modulo = len(rf[0]) - 1
breakpoint()
treeCounter = 0

horizPath = 3
vertPath = 1

lz = 0  # present horizontal location

def getHorizLoc(x):
    if lz % modulo == 0 and lz != 0:
        return modulo
    else:
        return lz % modulo

for line in rf:  # currently this increments vertical by 1
    hl = getHorizLoc(lz)
    indicator = ['^' if x == hl else ' ' for x in range(modulo)]
    indicator = ''.join(indicator)
    print(line + indicator)
    # check if tree
    if line[hl] == '#':
        treeCounter += 1
    # move to next location
    lz += horizPath

print(treeCounter)