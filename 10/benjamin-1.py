"""
Day 10
"""

def checklen(length, amount):
    if amount >= length:
        amount = amount - length
        return checklen(length, amount)
    return amount

INPUT = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
LENS = [int(x.strip()) for x in INPUT.split(',')]
LIST = [int(x) for x in range(0, 256)]
SKIP = 0
CURR = 0

for length in LENS:
    curr_values = []
    for n in range(0, length):
        indx = checklen(len(LIST), CURR + n)
        val = LIST[indx]
        curr_values.append(val)

    new_values = [int(x) for x in reversed(curr_values)]

    for n in range(0, length):
        indx = checklen(len(LIST), CURR + n)
        LIST[indx] = new_values[n]

    CURR =+ CURR + length + SKIP
    SKIP =+ SKIP + 1

print(LIST[0]*LIST[1])
