cmds = []

for i in range(int(input())) :
    cmds.append(input())

answer = ""

for i in range(len(cmds[0])) :
    check = 0
    for k in range(1, len(cmds)) :
        if cmds[0][i] == cmds[k][i] :
            check += 1
    if check == len(cmds) - 1 :
        answer += cmds[0][i]
    else :
        answer += "?"

print(answer)