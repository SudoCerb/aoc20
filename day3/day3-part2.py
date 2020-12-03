file = open('input.txt','r')
lines = file.readlines()
rf = []  # reference field
for line in lines:
    rf.append(line)

modulo = len(rf[0]) - 1

paths = [
    (3,1),
    (1,1),
    (5,1),
    (7,1),
    (1,2)
]

trees = []


def getHorizLoc(x):
    if x % modulo == 0 and x != 0:
        return 0
    else:
        return x % modulo

for path in paths:
    lz = 0  # present horizontal location
    horizPath = path[0]
    vertPath = path[1]
    treeCounter = 0
    for i in range(0,len(rf),vertPath):
        line = rf[i]
        hl = getHorizLoc(lz)
        indicator = ['^' if x == hl else ' ' for x in range(modulo)]
        indicator = ''.join(indicator)
        if line[hl] == '#':
            treeCounter += 1
        lz += horizPath
    print(f'Path {path} encounters {treeCounter} trees')
    trees.append(treeCounter)

def prod(iterable):
    answer = 1
    for x in iterable:
        answer = answer * x
    return answer
answer = prod(trees)
print(f"Answer: {answer}")

