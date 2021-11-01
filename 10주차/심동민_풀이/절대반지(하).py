'''
문제 : 절대반지
카테고리 : #string
'''


def solution(rings):
    i, j = 0, 0

    for _ in range(len(rings)+len(rings)-1):
        if i >= len(nickname)-1:
            return 1

        if nickname[i] == rings[j]:
            i += 1
        else:
            i = 0

        j += 1
        if j == len(rings):
            j = 0
    return 0


if __name__ == "__main__":
    nickname = input()
    numOfRing = int(input())
    rings = []

    ans = 0

    for i in range(numOfRing):
        ans += solution(input())

    print(ans)
