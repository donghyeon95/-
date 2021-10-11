import heapq

def dijkstra(graph, start, end):
    cost = [float('inf') for _ in range(len(graph))]  # start로부터 cost를 저장
    cost[start] = 0  # 시작값은 0
    queue = []
    heapq.heappush(queue, [cost[start], start])  # 시작 지점과 cost를 queue에 추가

    while queue:  # queue에 노드가 없을때까지 반복
        cur_cost, cur_node = heapq.heappop(queue)  # 탐색할 노드와 cost를 가져옴

        # 가져온 노드의 cost가 기존의 cost보다 길다면 pass
        if cost[cur_node] < cur_cost:
            continue

        for new_node, new_cost in graph[cur_node]:
            # 해당 노드를 거쳐 갈 때의 cost계산.
            # 해당 노드의 cost에 기존의 cost만큼을 더해줌
            new_cost += cur_cost

            # 기존의 cost 보다 작으면 갱신
            if new_cost < cost[new_node]:
                cost[new_node] = new_cost
                heapq.heappush(queue, [new_cost, new_node])  # 다음 node를 계산 하기 위해 큐에 삽입

    return cost[end]

# n = 지점의 개수, s는 출발지점
# a는 a의 도착지점, b는 b의 도착지점
# fares는 지점사이의 택시요금 [c,d,f]  << c와 d사이의 비용이 f
def solution(n, s, a, b, fares):
    answer = float("inf")

    # 인접 거리와 비용을 저장하기위한 list
    # index는 0부터 시작해서 n+1만큼
    graph = [[] for _ in range(n + 1)]

    # [c,d,f] << c와 d사이의 비용이 f
    for i, j, cost in fares:
        graph[i].append((j, cost))
        graph[j].append((i, cost))
    # graph에 아래와 같이 저장됨
    #  [[], [[4,10],[3,41],[5,24],[6,25]], [[4,66],[3,22]], [[5,24],[1,41],[2,22]], [[1,10],[6,50],[2,66]], [[3,24],[6,2],[1,24]], [[5,2],[4,50],[1,25]]]

    # 시작지점부터 공통지점까지의 거리, 공통지점부터 a, b까지의 거리의 합중 제일 작은값 return
    for i in range(1, n + 1):
        answer = min(answer, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))
    return answer