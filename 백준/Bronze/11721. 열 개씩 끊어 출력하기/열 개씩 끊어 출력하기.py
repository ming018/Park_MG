array = list(input())
print(array[0], end = '')
for i in range(1, len(array)) :
    
    if i % 10 == 0 :
        print('')
        print(array[i], end = '')
        continue

    print(array[i], end = '')