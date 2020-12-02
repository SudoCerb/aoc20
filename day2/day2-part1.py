file = open('input.txt','r')
lines = file.readlines()
isValid = []
lineCount = 0
for line in lines:
    elem = line.split(' ')
    limits = elem[0].split('-')
    letter = elem[1].replace(':','')
    passwd = elem[2]
    count = passwd.count(letter)
    lineCount += 1
    if count >= int(limits[0]) and count <= int(limits[1]):
        isValid.append(lineCount)

print(len(isValid))