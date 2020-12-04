file = open('input.txt','r')
lines = file.readlines()
rf = []
for line in lines:
    rf.append(line)
currentDoc = []
validPassports = 0
requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
readStop = False
for line in rf:
    if line == '\n':
        readStop = True
    else:
        currentDoc.append(line)
    if readStop == True:
        fieldValidation = []
        for field in requiredFields:
            for data in currentDoc:
                if field in data:
                    fieldValidation.append(field)

        if len(fieldValidation) == len(requiredFields):
            validPassports += 1
        currentDoc = []
        readStop = False
print(validPassports)