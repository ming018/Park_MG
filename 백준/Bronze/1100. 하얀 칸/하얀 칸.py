num = 0
for l in range(8) :
    check = list(input())
    if l in [0, 2, 4, 6] :
        for i in range(0, len(check), 2) :
            if check[i] == 'F' :
                num += 1
        continue
    
    for i in range(1, len(check), 2) :
            if check[i] == 'F' :
                num += 1
    
print(num)