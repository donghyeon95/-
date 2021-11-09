'''
문제 : 숫자 기차
카테고리 : #dp
'''


def solution(n):
    n = int(input())
    a = [0]+[1]*9
    b = [0]*10

    for _ in range(2, n+1):
        b[0] = a[1]
        b[9] = a[8]
        for i in range(1, 9):
            b[i] = a[i-1]+a[i+1]
        a = b[:]

    return sum(a) % 1000000000


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
