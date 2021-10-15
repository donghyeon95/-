def solution(n, diary_b):
    if n == 1:
        return diary_b

    result = []

    for i in range(n):
        diary_b[i] = diary_b[i] * (i+1)

    result.append(diary_b[0])

    for i in range(1, n):
        result.append(diary_b[i]-diary_b[i-1])

    return result


def main():
    n = int(input())
    diary_b = list(map(int, input().split()))

    print(*solution(n, diary_b))


if __name__ == '__main__':
    main()
