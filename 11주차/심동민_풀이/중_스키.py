'''
문제 : 스키
카테고리 : #dp
'''


def get_score_v2(n, m):
    global graph
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = graph[0][0]

    dx = [-1, 0]
    dy = [0, -1]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            temp = -float('inf')

            for k in range(len(dx)):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    temp = max(temp, dp[nx][ny])

            dp[i][j] = temp + graph[i][j]

    return dp[n-1][m-1]


def get_score(n, m):
    global graph
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = graph[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if 0 <= i < n and 0 <= j < m:
                up_cost = dp[i-1][j]
                left_cost = dp[i][j-1]
                dp[i][j] = max(graph[i][j] + up_cost, graph[i][j] + left_cost)
                continue

            if (i-1) < 0:
                dp[i][j] = graph[i][j] + dp[i][j-1]
                continue

            if (j-1) < 0:
                dp[i][j] = graph[i][j] + dp[i-1][j]
                continue

    return dp[n-1][m-1]


if __name__ == "__main__":

    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    print(get_score(n, m))
