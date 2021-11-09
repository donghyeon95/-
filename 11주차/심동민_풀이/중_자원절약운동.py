'''
문제 : 자원 절약 운동
카테고리 : #bfs
'''
from collections import defaultdict, deque


def bfs(node):
    global N, graph

    visited = [0] * (N+1)
    q = deque([(node, 1)])
    visited[node] = 1

    while q:
        cur, dist = q.popleft()

        for i in graph[cur]:
            if visited[i]:
                continue
            visited[i] = dist
            q.append((i, dist+1))

    return sum(visited) - 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(list)

    ans = float('inf')
    node = float('inf')

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        cost = bfs(i)

        if ans > cost:
            ans, node = cost, i
        elif ans == cost:
            node = min(node, i)

    print(node)
