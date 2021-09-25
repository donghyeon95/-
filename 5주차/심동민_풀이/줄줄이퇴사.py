def solution(n, work):
    work.sort()

    result = 0
    temp = work[0]
    for i in range(1, n):
        result += temp + work[i]
        temp = result

    return result


def main():
    n = int(input())
    work = []

    for _ in range(n):
        work.append(int(input()))

    print(solution(n, work))


if __name__ == '__main__':
    main()
