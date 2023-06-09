str_ = input()
leng = len(str_)
check = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in check :
    if i in str_ :
        leng -= str_.count(i)
print(leng)