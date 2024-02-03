humans = []

while True :
    name, age, weight = map(str, input().split())
    if name == "#" :
        break
    age = int(age)
    weight = int(weight)

    if age > 17 or weight >= 80 :
        grade = "Senior"
    else :
        grade = "Junior"

    humans.append([name, grade])

for i in humans :
    print(i[0], end = ' ')
    print(i[1])