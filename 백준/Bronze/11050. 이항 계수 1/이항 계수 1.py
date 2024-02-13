def fac(num):
    if num == 0:  # num이 0일 경우를 처리
        return 1
    elif num == 1:
        return num
    else:
        return num * fac(num - 1)

n, k = map(int, input().split())

print(int(fac(n) / (fac(k) * fac(n - k))))