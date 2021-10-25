from collections import defaultdict

t = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))


a_sum = []
for i in range(n):
    temp = 0
    for j in a[i:]:
        temp += j
        a_sum.append(temp)
print(a_sum)

b_sum_dict = defaultdict(int)
for i in range(m):
    temp = 0
    for j in b[i:]:
        temp += j
        b_sum_dict[temp] += 1
print(b_sum_dict.keys(), b_sum_dict.values())

cnt = 0
for a in a_sum:
    if t-a in b_sum_dict.keys():
        cnt += b_sum_dict[t-a]

print(cnt)
