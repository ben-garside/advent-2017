regs = {}
with open("c:\\Users\\garsideb\\Documents\\aoc\\08\\input.txt") as f:
    for line in f:
        reg, inst, amount, ifs, reg_test, test, quant = line.split()
        regs[reg] = 0

with open("c:\\Users\\garsideb\\Documents\\aoc\\08\\input.txt") as f:
    for line in f:
        reg, inst, amount, ifs, reg_test, test, quant = line.split()
        # print(reg, inst, amount, ifs, reg_test, test, quant)

        # print(regs[reg_test], test, quant)

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
        
        # print(testResult)
        if testResult:
            if inst == "dec":
                regs[reg] = regs[reg] - int(amount)
            elif inst == "inc":
                regs[reg] = regs[reg] + int(amount)

tst = []    
for v in regs:
    tst.append(regs[v])

print(max(tst))
