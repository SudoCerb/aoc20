import pandas as pd

CHECKED_RULES = []
VALID_COLOURS = []
TOTAL_BAGS = 0

lines = pd.read_csv('input.txt', header=None, sep='~')
lines = lines.rename(columns={0:'bag'})
lines['content'] = lines['bag'].str.replace('.+contain ','', regex=True)
lines['content'] = lines['content'].str.replace('.','')
lines['content'] = lines['content'].str.replace('\sbags','', regex=True)
lines['content'] = lines['content'].str.replace('\sbag','')
lines['content'] = lines['content'].str.replace('no other','')
lines['content'] = lines['content'].str.split(', ')
lines['bag'] = lines['bag'].str.replace(' bags contain.+','', regex=True)
lines = lines.set_index('bag')
RULES = lines.to_dict()
RULES = RULES['content']
for k, v in RULES.items():
    v = [x.strip() for x in v]
    RULES[k] = v

def delve(colour):
    """
    Accept a colour string as input, and determine how many bags that bag must
    contain.

    :param colour:
    :return:
    """
    bags = RULES[colour]
    print(colour,'|',bags)
    countBags = 0
    global TOTAL_BAGS
    if bags == ['']:
        return 0
    for bag in bags:
        theseBags = int(bag.split(' ')[0])
        countBags += theseBags
        countBags += theseBags * delve(' '.join(bag.split(' ')[1:]))
        TOTAL_BAGS += countBags
    return countBags

def traverse(rule, colour):
    """
    Accept a colour string as input, traverse the ruleset to find all bags that
     contain that colour bag.
    :param rule: dictionary key for the ruleset
    :param colour: colour being searched for
    :return:
    """
    if len(rule) == 0:
        return 0
    if colour in RULES[rule]:
        # print(k)
        VALID_COLOURS.append(k)
    for i in RULES[rule]:
        CHECKED_RULES.append(i)
        traverse(i, colour)

ans = delve('shiny gold')
print(TOTAL_BAGS)
