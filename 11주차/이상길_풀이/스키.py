from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

table = []
check = []
for y in range(n):
    temp = list(map(int,input().split()))
    check.append([0]*m)
    table.append(temp)
# ------  입력받기
if table[0][0] == 1:
    check[0][0] = 1

q=deque([(0,0)]) 
# y방향으로 +1 or x방향 +1 로만 움직일 수 있다.

while q:
    y,x = q.popleft()
    score = check[y][x]
    
    # 아래 방향 이동
    if 0<= y+1 <= n-1 and 0<= x+1 <= m-1:
        q.append((y+1,x))
        q.append((y,x+1))
        if table[y+1][x] == 1:
            check[y+1][x] = score + 1 if score+1 > check[y+1][x] else check[y+1][x]
        else:
            check[y+1][x] = score if score > check[y+1][x] else check[y+1][x]
        
        if table[y][x+1] == 1:
            check[y][x+1] = score + 1 if score+1 > check[y][x+1] else check[y][x+1]
        else:
            check[y][x+1] = score if score > check[y][x+1] else check[y][x+1]

    elif y == n-1 and 0 <= x+1 <= m-1:
        q.append((y,x+1))
        if table[y][x+1] == 1:
            check[y][x+1] = score + 1 if score+1 > check[y][x+1] else check[y][x+1]
        else:
            check[y][x+1] = score if score > check[y][x+1] else check[y][x+1]
    
    elif 0<= y+1 <= n-1 and x == m-1:
        q.append((y+1,x))
        if table[y+1][x] == 1:
            check[y+1][x] = score + 1 if score+1 > check[y+1][x] else check[y+1][x]
        else:
            check[y+1][x] = score if score > check[y+1][x] else check[y+1][x]
    
                

    

print(check[n-1][m-1])


