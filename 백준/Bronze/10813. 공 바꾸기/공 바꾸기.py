box_, count = map(int, input().split())
box = [(i + 1) for i in range(box_)]

for _ in range(count) :
    i, j = map(int, input().split())
    box[i - 1],box[j - 1] = box[j - 1], box[i - 1]

print(" ".join(str(i) for i in box))