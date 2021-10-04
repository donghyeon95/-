move = [(1,0), (0,1), (-1, 0), (0, -1)]

def change(queries, Map):
    
    y1, x1 = queries[:2]
    y2, x2 = queries[2:]
    
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    x , y = (x1, y1)
    
    
    stack = []
    point = 0
    
    while(True):

        stack.append(Map[y][x])
        if x == x1 and y == y1:
            Map[y][x] = Map[y+1][x]
        else:
            Map[y][x] = stack[-2]
            
        # 방향 전환
        if (x + move[point][0]) < x1 or (x + move[point][0]) > x2 or (y + move[point][1])< y1 or (y + move[point][1]) > y2:
            point += 1
            
        x += move[point][0]
        y += move[point][1]
        
                    
        if x == x1 and y == y1:
            break
        
        
    min_num = min(stack)
    return min_num  

def solution(rows, columns, queries):
    answer = []
    Map = [[i+columns*j+1 for i in range(columns)] for j in range(rows)]
    
    for i in queries:
        num = change(i,Map)

        answer.append(num)

        
    
    return answer
