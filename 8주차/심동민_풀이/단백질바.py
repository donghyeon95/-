n = int(input())

answer = []
for protein in [250, 40, 10]:
    q, r = divmod(n, protein)
    answer.append(q)
    n = r

if r:
    print(-1)
else:
    print(*reversed(answer))
