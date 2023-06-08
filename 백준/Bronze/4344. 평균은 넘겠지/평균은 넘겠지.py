for _ in range(int(input())) :
    nums = list(map(int, input().split()))
    ave = sum(nums[1 : ]) / nums[0]
    
    over = 0
    for i in nums[1 :] :
        if i > ave :
            over += 1
    
    print(f"{(over / nums[0]) * 100:.3f}%")