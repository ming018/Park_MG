array = input().split('-')
nums = []
sums = 0

for i in array :
    k = i.split('+')
    num = 0
    for j in k :
        num += int(j)
    nums.append(num)

sums = sum(nums[1 :])
print(nums[0] - sums)