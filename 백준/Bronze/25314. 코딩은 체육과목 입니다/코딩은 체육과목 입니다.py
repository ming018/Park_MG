num = int(input())
longs = ''

for _ in range((num // 4)) :
    longs += 'long '
longs += 'int'

print(longs)