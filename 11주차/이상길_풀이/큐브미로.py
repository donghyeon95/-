
import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    # L : 미로의 층 수 , R : 행, C : 열
    L,R,C = map(int,input().split())

    maze=[]
    visited = []
    temp=[]
    while True:
        wall = input()[:-1]
        if wall == "":
            continue

        if wall[0] == "0":
            break

        if wall != "":
            temp.append(wall)

    for i in range(R,(L*R)+1,R):
        maze.append(temp[i-R:i])
    # ------------------------------------ 입력 받기 및 maze 만들어 주기 
    # maze는 maze[층수(z)][행(y)][열(x)] 로 구성되어 있음
    # z 는 0~L-1사이의 범위, y는 0~R-1, x는 0~C-1 사이의 범위
    direction=[-1,1]
    q=deque()

    # 시작 위치 start
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if maze[z][y][x] == "S":
                    start = [z,y,x]
                    visited.append((z,y,x))
                    q.append((z,y,x,0))
                    break
    
    while q:
        z,y,x,cnt = q.popleft()

        for d in direction:
            if 0<= z + d <=L-1 and maze[z+d][y][x] == "E":
                    return print("탈출 성공 : {}분".format(cnt+1))

            if 0<= y+d <= R-1 and maze[z][y+d][x] == "E":
                    return print("탈출 성공 : {}분".format(cnt+1))

            if 0<= x+d <= C-1 and maze[z][y][x+d] == "E":
                    return print("탈출 성공 : {}분".format(cnt+1))

            if 0<= z + d <=L-1 and maze[z+d][y][x] == ".":    
                if (z+d,y,x) not in visited:
                    visited.append((z+d,y,x))
                    q.append((z+d,y,x,cnt+1))

            if 0<= y + d <=R-1 and maze[z][y+d][x] == ".":
                if (z,y+d,x) not in visited:
                    visited.append((z,y+d,x))
                    q.append((z,y+d,x,cnt+1))

            if 0<= x + d <=C-1 and maze[z][y][x+d] == ".":
                if (z,y,x+d) not in visited:
                    visited.append((z,y,x+d))
                    q.append((z,y,x+d,cnt+1))


    print("탈출 불가")


solve()






