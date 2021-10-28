'''
문제 : 책정리
카테고리 : #binary-search #dp
'''
import bisect


def LIS(n, books):
    dp = [books[0]]

    for i in range(n):
        if books[i] > dp[-1]:
            dp.append(books[i])
        else:
            idx = bisect.bisect_left(dp, books[i])
            dp[idx] = books[i]

    return n - len(dp)


if __name__ == "__main__":
    n = int(input())
    books = list(map(int, input().split()))

    print(LIS(n, books))
