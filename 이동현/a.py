
clock = [(1,0), (0,-1), (-1,0), (0, 1)]
unclock = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def f_unclock(res, n, angle):
    pass

def f_clock(res, n, angle, cnt):
    num = 1
    for idx, (dx, dy) in enumerate(clock):
        print(idx)
        x = angle[idx][0]
        y = angle[idx][1]

        while num < n-1:
            res[y+dy][x+dx] = cnt 
            cnt += 1
            num += 1

    new_angle = [
        (angle[0]+1, angle[1]+1), 
        (angle[1]-1, angle[1]+1), 
        (angle[2]+1, angle[2]-1),
        (angle[3]-1, angle[3]-1)
    ]

    f_clock(res, n-2, new_angle, cnt)
    

def solution(n, clockwise):
    res = [[0 for _ in range(n)] for _ in range(n)]
    angle = [(0,0), (n-1, 0), (0, n-1), (n-1, n-1)]

    if n == 1:
        return [1]
    if n == 2:
        return [[1,1], [1,1]]

    if clockwise:
        f_clock(res, n, angle, 1)
        return res
    
    if not clockwise:
        # f_unclock(res, n, angle, 1)
        return res