import re

def validate(field, line):
    if field == 'ecl':
        match = re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)', line)
        if match:
            return True
    elif field == 'pid':
        match = re.search('pid:\d{9}(\\n| |\')', line)
        if match:
            return True
    elif field == 'eyr':
        match = re.search('eyr:(\d{4})', line)
        if match:
            out = match.group(0)
            out = int(out.split(':')[1])
            if 2020 <= out <= 2030:
                return True
    elif field == 'hcl':
        match = re.search('hcl:#([a-f0-9]){6}', line)
        if match:
            return True
    elif field == 'byr':
        match = re.search('byr:(\d{4})', line)
        if match:
            out = match.group(0)
            out = int(out.split(':')[1])
            if 1920 <= out <= 2002:
                return True
    elif field == 'iyr':
        match = re.search('iyr:(\d{4})', line)
        if match:
            out = match.group(0)
            out = int(out.split(':')[1])
            if 2010 <= out <= 2020:
                return True
    elif field == 'hgt':
        match = re.search('hgt:\d+(cm|in)', line)
        if match:
            out = match.group(0)
            out = out.split(':')[1]
            if 'cm' in out:
                out = int(out.split('cm')[0])
                if 150 <= out <= 193:
                    return True
            elif 'in' in out:  # this is implicit, could just be "else"
                out = int(out.split('in')[0])
                if 59 <= out <= 76:
                    return True
    return False

file = open('input.txt','r')
lines = file.readlines()
rf = []
for line in lines:
    rf.append(line)
currentDoc = []
validPassports = 0
requiredFields = ['byr', 'pid', 'eyr', 'hcl', 'ecl', 'iyr', 'hgt']
readStop = False
for line in rf:
    if line == '\n' or line == '':
        readStop = True
    else:
        currentDoc.append(line)
    if readStop == True:
        # breakpoint()
        fieldValidation = []
        for data in currentDoc:
            for field in requiredFields:
                if field in data:
                    if validate(field, data):
                        fieldValidation.append(field)

        if set(fieldValidation) == set(requiredFields):
            validPassports += 1
            print(currentDoc)
        currentDoc = []
        readStop = False
# handle end case
if (currentDoc != []) and readStop == False:
    fieldValidation = []
    for data in currentDoc:
        for field in requiredFields:
            if field in data:
                if validate(field, data):
                    fieldValidation.append(field)

    if set(fieldValidation) == set(requiredFields):
        validPassports += 1
        print(currentDoc)
print(validPassports)