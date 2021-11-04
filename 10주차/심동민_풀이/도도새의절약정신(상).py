'''
문제 : 도도새의 절약 정신
카테고리 : #그리디
'''

if __name__ == '__main__':
    n, k = map(int, input().split())
    times = list()
    gaps = list()

    for n in range(n):
        times.append(int(input()))

    for n in range(n-1):
        gaps.append(times[n+1] - times[n] - 1)

    gaps.sort()
    ans = n
    for i in range(n-k):
        ans += gaps[i]
    print(ans)
