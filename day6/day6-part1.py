lines = open('input.txt','r').read().splitlines()

yesCount = 0

groups = []
curGroup = []
for line in lines:
    if len(line) > 0:
        curGroup.append(line)
    else:
        groups.append(set(''.join(curGroup)))
        curGroup = []
else:
    groups.append(set(''.join(curGroup)))
    curGroup = []
for curGroup in groups:
    yesCount += len(curGroup)
print(yesCount)
