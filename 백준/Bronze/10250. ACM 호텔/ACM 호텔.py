for _ in range(int(input())) :
    h, w, n = map(int, input().split())
    room = 1
    num = 100 + room
    for _ in range(n - 1) :
        num += 100
        if num > (100 * h) + 100 :
            room += 1
            num = 100 + room
    print(num)