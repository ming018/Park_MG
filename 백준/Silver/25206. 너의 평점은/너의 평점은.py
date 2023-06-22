import sys

count = 0.0
sum_ = 0.0
grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': 0.0}

for _ in range(20):
    array = sys.stdin.readline().split()
    
    if array[2] == 'P':
        continue

    sum_ += (grades[array[2]] * float(array[1]))
    count += float(array[1])

print(sum_ / count)