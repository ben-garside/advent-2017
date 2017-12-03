def one():
    number = 0
    with open("c:\\Users\\garsideb\\Documents\\aoc\\03\\input.txt") as f:
        for row in f:
            values = [int(x) for x in row.split()]
            number += max(values) - min(values)
    return number

def two():
    number = 0
    with open("c:\\Users\\garsideb\\Documents\\aoc\\03\\input.txt") as f:
        for row in f:
            values = [int(x) for x in row.split()]
            for value in values:
                for secondValue in values:
                    if secondValue != value:
                        if value % secondValue == 0:
                            n = value / secondValue
                            number += (int(n))
    return number


print("One: %s" % one())
print("Two: %s" % two())
