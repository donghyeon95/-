n = int(input())

num = list(range(1, n))

answer = 0

for i in num:
    if not i % 3:
        answer += i
        continue
    if not i % 5:
        answer += i

print(answer)
