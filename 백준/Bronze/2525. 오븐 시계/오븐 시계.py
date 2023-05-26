hour, min_ = map(int, input().split())
time = int(input())

if time + min_ >= 60 :
    hour += (time + min_) // 60
    if hour >= 24 :
        hour -= 24
    min_ += time - (60 * ((time + min_) // 60))
    
else : min_ += time

print(hour, min_)