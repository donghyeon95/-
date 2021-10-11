import math
import itertools
import copy
import collections
def getPoint(board,curr):
    res = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == curr:
                res.append((i,j))
    return res[0],res[1]

def build(board):
    graph = [[math.inf]* (4*4) for _ in range(4*4)]
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            if j != 0:
                graph[idx][idx - 1] = 1
            if j != 3:
                graph[idx][idx + 1] = 1
            if i != 0:
                graph[idx][idx - 4] = 1
            if i != 3:
                graph[idx][idx + 4] = 1
            k = j-1
            while k >= 0:
                if board[i][k] > 0:
                    graph[idx][i * 4 + k] = 1
                    break
                elif board[i][k] == 0 and k == 0:
                    graph[idx][i*4] = 1
                    break
                k -= 1
            k = j+1
            while k < 4:
                if board[i][k] > 0:
                    graph[idx][i * 4 + k] = 1
                    break
                elif board[i][k] == 0 and k == 3:
                    graph[idx][i * 4 + k] = 1
                    break
                k += 1
            k = i-1
            while k >= 0:
                if board[k][j] > 0:
                    graph[idx][k * 4 + j] = 1
                    break
                elif board[k][j] == 0 and k == 0:
                    graph[idx][j] = 1
                    break
                k -= 1
            k = i+1
            while k < 4:
                if board[k][j] > 0:
                    graph[idx][k * 4 + j] = 1
                    break
                elif board[k][j] == 0 and k == 3:
                    graph[idx][k * 4 + j] = 1
                    break
                k += 1
    return graph

def bfs(s,e,g):
    i,j = s
    sid = i * 4 + j
    i,j = e
    eid = i * 4 + j
    q = collections.deque()
    q.append(sid)
    parents = [-1] * (4*4)
    while len(q) != 0:
        i = q.popleft()
        for j in range(4*4):
            if parents[j] == -1 and g[i][j] != math.inf:
                parents[j] = i
                q.append(j)
    cnt = 0
    while eid != sid:
        eid = parents[eid]
        cnt += 1
    return cnt

def dist(p1,p2, board, cursor):
    graph = build(board)
    return bfs(cursor,p1,graph) + bfs(p1,p2,graph) + 2 

def calc(board, st, cursor):
    if len(st) == 0:
        return 0
    b = copy.deepcopy(board)
    s = copy.deepcopy(st)
    curr = s.pop()
    p1,p2 = getPoint(board,curr)
    d1 = dist(p1,p2,b,cursor)
    d2 = dist(p2,p1,b,cursor)
    i, j = p1
    b[i][j] = 0
    i,j = p2
    b[i][j] = 0 
    return min(d1 + calc(b,s,p2), d2 + calc(b,s,p1))

def solution(board,r,c):
    s = set()
    for i in range(4):
        for j in range(4):
            s.add(board[i][j])
    s.remove(0)
    answer = math.inf
    for st in itertools.permutations(s):
        answer = min(answer,calc(board,list(st),(r,c)))
    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))