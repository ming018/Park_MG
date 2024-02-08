from collections import deque

N, K = map(int, input().split())
yosepus = deque(range(1, N+1))
answer = []

K_ = 0

while len(yosepus) > 1:

    if K_ < K - 1:
        yosepus.append(yosepus.popleft())
        K_ += 1
        continue

    answer.append(yosepus.popleft())
    K_ = 0

answer.append(yosepus.popleft())

print("<",end="")
for i in range(len(answer) - 1):
    print(answer[i],end=", ")

print(answer[len(answer) - 1], end = ">")