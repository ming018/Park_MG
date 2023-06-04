# 미리 계산된 값을 저장할 2차원 배열 생성
apart = [[0 for _ in range(15)] for _ in range(15)]

# 초기 값 설정
for i in range(15):
    apart[i][0] = 1
    apart[0][i] = i + 1

# 사람 수 계산
for i in range(1, 15):
    for k in range(1, 15):
        apart[i][k] = apart[i][k - 1] + apart[i - 1][k]

count = int(input())
output = []

for _ in range(count):
    floor = int(input())
    num = int(input())
    output.append(str(apart[floor][num - 1]))

print("\n".join(output))
