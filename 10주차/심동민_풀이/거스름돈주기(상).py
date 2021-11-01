'''
문제 : 거스름돈 주기
카테고리 : #dp
'''


def solution(n, money, target):
    dp = [[1 if not i else 0 for i in range(target+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(1, target + 1):
            if j >= money[i]:
                dp[i][j] = dp[i-1][j] + dp[i][j - money[i]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n-1][target]


if __name__ == '__main__':
    n = int(input())
    money = list(map(int, input().split()))
    target = int(input())

    print(solution(n, money, target))
