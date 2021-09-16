def solution(r, c, k):
    if k == 1:
        return 1
    if (r * c) % 2 == 0:
        return 1
    else:
        return 0


def main():
    r, c, k = map(int, input().split())

    print(solution(r, c, k))


if __name__ == '__main__':
    main()
