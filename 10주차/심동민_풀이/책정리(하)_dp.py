'''
문제 : 책정리
카테고리 : #dp
'''


def LIS(n, books):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if books[i] > books[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return n - max(dp)


if __name__ == "__main__":
    n = int(input())
    books = list(map(int, input().split()))
    print(LIS(n, books))
