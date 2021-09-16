from collections import deque


def solution(coins):
    front, back = 0, 0

    side = coins[0]
    que = deque(coins[1:])

    while que:
        cur = que.popleft()

        if side == cur:
            continue

        elif side != cur:
            if side == '0':
                front += 1
            else:
                back += 1
            side = cur

    if cur == '0':
        front += 1
    else:
        back += 1

    return min(front, back)


def main():
    coins = list(input())

    print(solution(coins))


if __name__ == '__main__':
    main()
