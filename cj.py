cases = input()

for case in range(int(cases)):
    x, y, mural = input().split(" ")
    x = int(x) #cj
    y = int(y) #jc
    min_val = min(x,y)

    #print(x, y, mural)
    last_char = ''
    cost = 0
    for index in range(len(mural)):
        if mural[index] == 'C' and last_char == '':
            last_char = 'C'
        elif mural[index] == 'J' and last_char == '':
            last_char = 'J'
        elif mural[index] == 'C' and last_char == 'J':
            cost += y
            last_char = 'C'
        elif mural[index] == 'J' and last_char == 'C':
            cost += x
            last_char = 'J'
        else:
            pass
    print("Case #"+ str(case+1)+ ": "+ str(cost))