x, y, w, h = map(int, input().split())

wx = w - x

hy = h - y

if x > y :
    compare = y
else :
    compare = x

if wx < hy :
    result = wx
    if result > x :
        answer = x
    else :
        answer = result
else:
    result = hy

    if result > y :
        answer = y
    else :
        answer = result

if answer < compare :
    print(answer)
else :
    print(compare)
