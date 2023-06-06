str_ = list(input())
answer = 1

for i in range(len(str_) // 2) :
    if str_[i] != str_[-(i + 1)] :
        answer = 0
        break
print(answer)
