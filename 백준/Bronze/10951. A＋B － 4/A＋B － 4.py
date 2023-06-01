array = []

while(1):
    try :
        array.append(sum(map(int, input().split())))
    except :
        break
    
for i in array :
    print(i)