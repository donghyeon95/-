

def solution(index, Graph, visited):
    queue = [(index,0)]
    res = 0
    while True:
        if len(queue) == 0:
            break
#         print(queue)
        
        node, depth = queue.pop(0)
        
        
        if visited[node] is not 0:
                continue
                
        visited[node] = 1
        res += depth
        # print(node, depth, res)
        
            
        for N in Graph[node]:
            if visited[N] is not 0: 
                continue
            queue.append((N, depth+1))
                

    return res



if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    Graph = [[] for _ in range(N+1)]
    result = [0 for _ in range(N+1)]
    
    for _ in range(M):
        x, y = list(map(int, input().split()))
        Graph[x].append(y)
        Graph[y].append(x)
    
    for i in range(1, N+1):
        result[i] = solution(i, Graph, [0 for _ in range(N+1)])

    min_num = min(result[1:])
    print(result.index(min_num))