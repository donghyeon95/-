price = int(input())

change = 10000 - price

total = 0


for i in [10000, 1000,  100, 10, 1]:
    result = divmod(change, i)

    total += result[0]
    change = result[1]

print(total)


'''
숏코딩
'''
print(sum(map(int, str(10000-int(input())))))
