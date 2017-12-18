steps = []
registers = {}
last_played = {}

with open("c:\\Users\\garsideb\\Documents\\aoc\\18\\input.txt") as f:
    for row in f:

        instruction, register = row.split()[:2]
        value = None

        if len(row.split()) == 3:
            value = row.split()[2]
        else:
            vlaue = None

        try:
            value = int(value)
        except:
            pass
        
        try:
            register = int(register)
        except:
            pass

        if isinstance(register, str):
            registers[register] = 0
            last_played[register] = 0
        steps.append([instruction, register, value])

i = 0
run = True 

while run == True:

    instruction, register, value = steps[i]
    move = False

    if instruction == "snd":
        last_played[register] = registers[register]

    if instruction == "set":
        if isinstance(value, int):
            registers[register] = value
        else:
            registers[register] = registers[value]

    if instruction == "add":
        if isinstance(value, int):
            registers[register] = registers[register] + value
        else:
            registers[register] = registers[register] + registers[value]

    if instruction == "mul":
        if isinstance(value, int):
            registers[register] = registers[register] * value
        else:
            registers[register] = registers[register] * registers[value]

    if instruction == "mod":
        if isinstance(value, int):
            registers[register] = registers[register] % value
        else:
            registers[register] = registers[register] % registers[value]

    if instruction == "rcv":
        last_plyed_freq = last_played[register]
        if last_plyed_freq != 0:
            run = False
            print("LAST PLAYED [%s]: %s" % (register, last_plyed_freq))

    if instruction == "jgz":
        if isinstance(value , int):
            jump = value
        else:
            jump = registers[value]

        if isinstance(register, int):
            check = register
        else:
            check = registers[register]

        if check > 0:
            move = i + jump

    if move:
        i = move
    else:
        i = i + 1
