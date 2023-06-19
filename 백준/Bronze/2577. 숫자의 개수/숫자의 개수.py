nums = []
for _ in range(3) :
    nums.append(int(input()))
num = nums[0] * nums[1] * nums[2]

counting = list(0 for _ in range(10))

num = list(str(num))

for i in num :
    counting[int(i)] += 1

[print(x) for x in counting]