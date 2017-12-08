import operator

regs = {}
max_num = 0


def check_max(A, max_num):
    tst = []    
    for v in A:
        tst.append(A[v])
    new_max = max(tst)
    if int(new_max) > int(max_num):
        max_num = new_max
    return max_num


with open("c:\\Users\\garsideb\\Documents\\aoc\\08\\input.txt") as f:
    for line in f:
        reg, inst, amount, ifs, reg_test, test, quant = line.split()
        regs[reg] = 0

with open("c:\\Users\\garsideb\\Documents\\aoc\\08\\input.txt") as f:
    for line in f:
        reg, inst, amount, ifs, reg_test, test, quant = line.split()

        if  test == "!=":
            testResult = int(regs[reg_test]) != int(quant)
        elif test == ">":
            testResult =int(regs[reg_test]) > int(quant)
        elif test == "<":
            testResult =int(regs[reg_test]) < int(quant)
        elif test == "==":
            testResult =int(regs[reg_test]) == int(quant)
        elif test == ">=":
            testResult =int(regs[reg_test]) >= int(quant)
        elif test == "<=":
            testResult =int(regs[reg_test]) <= int(quant)
        else:
            print("ERROR!!!")
        
        if testResult:
            if inst == "dec":
                regs[reg] = regs[reg] - int(amount)
            elif inst == "inc":
                regs[reg] = regs[reg] + int(amount)

        max_num = check_max(regs, max_num)

print(max_num)
