file = open('input.txt','r')
lines = file.readlines()
isValid = []
lineCount = 0
for line in lines:
    elem = line.split(' ')
    locations = elem[0].split('-')
    locations = [int(x) - 1 for x in locations]
    letter = elem[1].replace(':','')
    passwd = elem[2]
    counts = 0
    lineCount += 1
    if passwd[int(locations[0])] == letter and passwd[int(locations[1])] == letter:
        pass
    elif passwd[int(locations[0])] == letter or passwd[int(locations[1])] == letter:
        isValid.append(lineCount)

print(len(isValid))
