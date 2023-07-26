num1, num2 = map(list, input().split())

num1.reverse()
num2.reverse()

num1 = ''.join(map(str, num1))
num1 = int(num1)

num2 = ''.join(map(str, num2))
num2 = int(num2)

num = num1 + num2

num = list(str(num))
num.reverse()
num = ''.join(map(str, num))

num = int(num)

print(num)