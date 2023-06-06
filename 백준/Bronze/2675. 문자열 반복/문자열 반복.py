array = []
for i in range(int(input())) :
    num, str_ = input().split()
    str_ = list(str_)
    print(*(str_.pop(0) * int(num) for _ in range(len(str_))), sep='')