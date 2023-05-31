num1, num2 = map(int,input().split())

array = []
for i in range(num1) :
    array.append(i + 1)

for _ in range(num2) :
    begin, end, mid = map(int, input().split())
    array = array[ : begin - 1] + array[mid - 1 : end] + array[begin - 1 : mid - 1] + array[end :]

str_ = ""

for _ in range(num1) :
    str_ += str(array.pop(0)) + " "

print(str_)