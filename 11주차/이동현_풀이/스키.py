'''
def solution(x, y, N, M, ski):

    # 재귀로 풀면 시간이 많이 걸림... memo를 쓰면 되지만 그것보다는 그냥 역으로 계산하는 것이 더 빠를 듯 하다. 
    res = 0
    
    if x+1 >=N and y+1 <M:
        res = ski[x][y] + solution(x,y+1, N, M, ski)
    elif y+1 >=M and x+1 <N:
        res = ski[x][y] + solution(x+1,y, N, M, ski)
    elif x+1 >=N and y+1 >=M:
        res = ski[x][y]
    else:
        res = ski[x][y] + max(solution(x,y+1, N, M, ski), solution(x+1,y, N, M, ski))
        
    return res
'''

 

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    ski = [list(map(int,input().split())) for _ in range(N)]
    
    MAP = [[0 for _ in range(M)] for _ in range(N)]
    MAP[N-1][M-1] = ski[N-1][M-1]

    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):

            if y==N-1 and x==M-1:
                continue
            if y+1>=N and x+1<M:
                MAP[y][x] = ski[y][x] + MAP[y][x+1]
            elif x+1>=M and y+1<N:
                MAP[y][x] = ski[y][x] + MAP[y+1][x]
            else:   
                MAP[y][x] = ski[y][x] + max(MAP[y+1][x], MAP[y][x+1])
            
            
    print(MAP[0][0])