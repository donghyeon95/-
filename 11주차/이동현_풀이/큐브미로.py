
'''
##질문거리##
1-1. 이런 배열 집어넣는 방법
1-2. 배열 말고 효율적으로 관리할 수 있는 지?
2.효율적으로 인자 전달 할 수 있는 방법??
''' 

def solution(floor, row, col, Maze, isvisited, *limit):
    
    
    if floor<0 or floor>=limit[0] or row<0 or row>=limit[1] or col<0 or col>=limit[2]:
        return float("inf")
    if Maze[floor][row][col] == '#':
        isvisited[floor][row][col] = float("inf")
        return float("inf")
    if isvisited[floor][row][col] != 0:
        return isvisited[floor][row][col]
        
    # print("si",isvisited)
    if Maze[floor][row][col] == 'E':
        isvisited[floor][row][col] = 1
        return 1
    
    res = float("inf")
    
    
    for move in Moves:
        l,r,c= [k+m for k,m in zip([floor,row,col], move)]
        res = min(res, solution(l,r,c, Maze, isvisited, L,R,C))
        # print(res)
        isvisited[floor][row][col] = res+1       
        
        
    return res + 1

if __name__ == "__main__":
    
    L, R, C = list(map(int, input().split()))
    l, r, c = [0,0,0]
    # Maze = [[list(input()) for string in range(R+1)] for _ in range(L)]
    
    #  # 공백 제거
    # for f in range(L):
    #     Maze[f].pop(-1)
    global move
    Moves = [[0,0,1],[0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]
    
    isvisited = [[[0 for _ in range(C)]for _ in range(R)]for _ in range(L)]
    
    Maze = [[[]for _ in range(R)]for _ in range(L)]
    res = float("inf")
    
    for f in range(L):
        for row in range(R):
            temp = list(input())
            for col in range(C):
                if temp[col] == 'S':
                    l = f
                    r = row
                    c = col
                Maze[f][row].append(temp[col])
        
        input()    
    
    for i in Moves:
        l,r,c= [k+m for k,m in zip([l,r,c], i)]
        res = min(res, solution(l,r,c, Maze, isvisited, L,R,C))
        
        
    if res == float("inf"):
        print("탈출 불가")
    else:
        print("탈출 성공 : {0}분".format(res))