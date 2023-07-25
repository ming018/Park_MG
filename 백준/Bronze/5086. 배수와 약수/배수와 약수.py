import sys

num1, num2 = map(int, sys.stdin.readline().split())

while(num1 != 0 and num2 != 0) :
    if num1 >= num2 :
        if num1 % num2 == 0 :
            print('multiple')
        else :
            print('neither')

    else :
        if num2 % num1 == 0 :
            print('factor')
        else :
            print('neither')

    num1, num2 = map(int, sys.stdin.readline().split())