box_, count = map(int, input().split())
box = [0 for _ in range(box_)]

for _ in range(count) :
    i, j, k = map(int, input().split())
    box[i - 1: j] = [k] * ((j - i) + 1)

print(" ".join(str(i) for i in box))