def one():
    with open("c:\\Users\\garsideb\\Documents\\aoc\\05\\input.txt") as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content] 
    curr_idex = 0
    count = 0
    out = False
    while out == False:
        if 0 <= curr_idex < len(content):
            count = count + 1
            next_idex = content[curr_idex] + curr_idex
            content[curr_idex] = content[curr_idex] + 1
            curr_idex = next_idex
        else:
            out = True
            print('Failed at step: %s' % count)


def two():
    with open("c:\\Users\\garsideb\\Documents\\aoc\\05\\input.txt") as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content] 
    curr_idex = 0
    count = 0
    out = False
    while out == False:
        if 0 <= curr_idex < len(content):
            count = count + 1
            next_idex = content[curr_idex] + curr_idex
            if content[curr_idex] > 2:
                content[curr_idex] = content[curr_idex] - 1
            else:
                content[curr_idex] = content[curr_idex] + 1
            curr_idex = next_idex
        else:
            out = True
            print('Failed at step: %s' % count)

one()
two()
