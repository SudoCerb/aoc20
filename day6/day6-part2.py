lines = open('input.txt','r').read().splitlines()

yesCount = 0
count = 1

groups = []
curGroup = []
breakpoint()
for line in lines:
    if len(line) > 0:
        curGroup.append(line)
    else:
        curGroup = [set(x) for x in curGroup]
        outSet = set()
        newGroup = True
        for ans in curGroup:
            if len(outSet) == 0 and newGroup:
                outSet = ans
                newGroup = False
            else:
                outSet = outSet & ans
        groups.append(outSet)
        print(count, outSet)
        curGroup = []
        count += 1
else:
    if curGroup == []:
        pass
    curGroup = [set(x) for x in curGroup]
    outSet = set()
    newGroup = True
    for ans in curGroup:
        if len(outSet) == 0 and newGroup:
            outSet = ans
            newGroup = False
        else:
            outSet = outSet & ans
    groups.append(outSet)
    print(count, outSet)
    curGroup = []
    count += 1
for curGroup in groups:
    yesCount += len(curGroup)
print(yesCount)