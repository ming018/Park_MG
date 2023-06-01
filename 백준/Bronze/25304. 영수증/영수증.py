total_price = int(input())
catalog = int(input())
check_price = 0

for _ in range(catalog) :
    price, num = map(int,input().split())
    check_price += price * num

print("Yes") if check_price == total_price else print("No")