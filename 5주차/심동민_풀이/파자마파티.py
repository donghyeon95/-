
import collections
import sys
from typing import Deque


def solution(n: int, k: int, m: int) -> int:
    """하트 여왕이 몇 번째로 원에서 나가는지 알아내는 프로그램

    Args:
        n (int): 친구 수
        k (int): k번째 수
        m (int): 하트 여왕의 번호

    Returns:
        int: 하트여왕의 나가는 순서
    """
    result = 0

    que: Deque = collections.deque(range(1, n+1))

    while que:
        for i in range(k-1):
            temp = que.popleft()
            que.append(temp)

        out = que.popleft()
        result += 1
        if out == m:
            break

    return result


def main():
    input = sys.stdin.readline
    n, k, m = map(int, input().split())

    print(solution(n, k, m))


if __name__ == '__main__':
    main()
