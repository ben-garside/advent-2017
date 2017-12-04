def one():
    number = 0
    with open("input.txt") as file:
        for line in file:
            values = line.split()
            test = 0
            for value in values:
                for testValue in values:
                    if value == testValue:
                        test = test + 1
            if test == len(values):
                number = number + 1              
    return number

def two():
    number = 0
    with open("input.txt") as file:
        for line in file:
            values = line.split()
            test = 0
            for value in values:
                for testValue in values:
                    if ''.join(sorted(value)) == ''.join(sorted(testValue)):
                        test = test + 1
            if test == len(values):
                number = number + 1       
    return number

print(one())
print(two())
