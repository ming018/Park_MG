limit = int(input())
cnt = limit

for _ in range(limit) :
    str_ = list(input())
    for i in range(len(str_) - 1) :
        if str_[i] == str_[i + 1] :
            continue
        if str_[i] in str_[i + 1 :] :
            cnt -= 1
            break
print(cnt)