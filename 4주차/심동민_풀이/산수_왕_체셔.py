a, b, c = map(int, input().split())


def solution(a, b, c):
    # 모듈러 연산 분배법칙
    if b == 1:
        return a % c

    if not b % 2:
        return solution(a, b//2, c) ** 2 % c
    else:
        return (solution(a, b//2, c) ** 2) * a % c


print(solution(a, b, c))
