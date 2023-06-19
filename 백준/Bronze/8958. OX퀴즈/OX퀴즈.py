for _ in range(int(input())):
    array = list(input())
    score = 0
    bonus = 1
    for i in array :
        if i == 'O' :
            score += bonus
            bonus += 1
        else :
            bonus = 1
    print(score)