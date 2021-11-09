
from collections import deque

n,m = map(int,input().split())

table = [[] for i in range(n+1)]

# 양방향 테이블 만들기
for _ in range(m):
    a,b = map(int,input().split())
    table[a].append(b)
    table[b].append(a)

# result에는 순서대로 도시 1의 교류관계~ 도시 n까지 들어갈 예정
result=[]

# i는 타겟 도시 즉 1부터~n 까지를 살펴볼 예정 temp에 각 도시 별 교류관계를 담아 sum(temp)로 result에 append할 예정
for i in range(1,n+1):
    temp = []
# j는 타겟 도시를 제외한 나머지 도시 들이 될 예정임
    for j in range(1,n+1):
        if i == j:
            continue
        else:
            q= deque()
            # queue에 타겟 도시에서 갈 수 있는 도시들을 담아줌
            for num in table[i]:
                q.append((1,num))
            check = [False] * (n+1)
            check[0] = True
            check[i] = True
            # check리스트를 활용하여 방문했는지 안했는지 확인해주고 bfs 해줌
            # 단점은 할 때마다 초기화 해야한다는 것임 중복되는 부분들을 좀 더 좋게 처리해주는 방법...?
            while q:
                cnt, target = q.popleft()
                if target == j:
                    temp.append(cnt)
                    break
                elif target != j and check[target] == False:
                    for targets in table[target]:
                        q.append((cnt+1,targets))
                    check[target] = True
    result.append(sum(temp))

for idx,val in enumerate(result):
    if val == min(result):
        print(idx+1)
        break

