N ,K = list(map(int, input().split()))

time = []
for i in range(N):
    time.append(int(input()))
    


#인접한 수와의 차이를 저장한다.
diff = []
for i in range(N-1):
    diff.append(time[i+1]-time[i])

diff.sort(reverse=True)


if len(diff) >= K:
    print(sum(diff[K-1:]) + K)
else:
    print(N)