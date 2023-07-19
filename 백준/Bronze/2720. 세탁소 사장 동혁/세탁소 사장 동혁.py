import sys

for _ in range(int(sys.stdin.readline())) :
    num = int(sys.stdin.readline())
    Q = 0
    D = 0
    N = 0
    P = 0
    
    Q += int(num // 25)
    num = num % 25

    D += int(num // 10)
    num = num % 10

    N += int(num // 5)
    num = num % 5

    P += int(num // 1)
    num = num % 1

    print(Q, D, N, P)