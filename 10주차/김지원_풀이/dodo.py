n,k = map(int,input().split())
t = []
for i in range(n):
    t.append(int(input()))
d = []
res = []
temp = 999999999
if k == len(t):
    print(k)
elif k == 1:
    print(max(t))
else:
    #초의수가 없을때, 경우의수증가
    for i in range(len(t)-1,0,-1):
        d.append(t[i]-t[i-1])
        temp = min(temp,(t[i] - t[i-1]))
    if k == (len(t) -1):
        res.append(temp+k)
    for i in range(1,k):
        di = d.index(temp)
    print(min(res))
