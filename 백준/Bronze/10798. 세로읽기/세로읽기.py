array = []
str_ = ''

for _ in range(5) :
    array.append(list(map(str, input())))

max_ = 0
for i in range(len(array)) :
    if len(array[i]) > len(array[max_]) :
        max_ = i

for i in range(len(array[max_])) :
    for k in range(len(array)) :
        if i >= len(array[k]) :
            continue
        str_ += str(array[k][i])
        
    
print(str_)