import sys

nums = []

for _ in range(int(sys.stdin.readline())) :
    num = int(sys.stdin.readline())
    if num != 0 :
        nums.append(num)
    else :
        nums.pop()

print(sum(nums))