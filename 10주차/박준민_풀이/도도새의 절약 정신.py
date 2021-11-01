n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(int(input()))
    
# 친구가 방문하는 시간의 차를 계산
t_diff = []
for i in range(n-1):
    t_diff.append((t[i+1]) - t[i]) # t_diff = [2, 3]
    
# 시간이 짧은 순서대로 정렬
t_diff.sort()
# print(t_diff)

# 최소 k번 만큼은 난로를 켜기때문에 초기값 설정
res = k
# 성냥이 부족한 만큼 t_diff만큼 추가
for i in range(n - k):
    res += t_diff[i]
print(res)
