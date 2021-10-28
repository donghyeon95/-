'''
문제 : 사냥꾼도도새
카테고리 : #dp
'''
from collections import deque, defaultdict


def solution(n: int, spider: list[int]) -> int:
    """거미를 잡기 위한 최소 총알 개수를 반환하는 함수

    Args:
        n (int): 거미의 수
        spider (list[int]): i번째 거미의 높이리스트

    Returns:
        int: 최대 총알 개수
    """

    # i번째까지 거미를 제거하기 위해 필요한 총알의 개수
    dp = [0] * n
    # 총알 높이 : 총알 개수
    bullet_list = defaultdict(int)

    # 초기값 세팅
    dp[0] = (1)
    bullet_list[spider[0] - 1] += 1

    for i in range(1, n):
        # 거미 높이에 해당하는 bullet가 존재한다면
        height = spider[i]
        if height in bullet_list and bullet_list[height] > 0:
            bullet_list[spider[i]] -= 1
            bullet_list[spider[i]-1] += 1

            dp[i] = dp[i-1]
        # 거미 높이에 해당하는 bullet이 없다. = 새로운 총알필요
        else:
            bullet_list[height-1] += 1

            dp[i] = dp[i-1] + 1

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    spider = list(map(int, input().split()))

    print(solution(n, spider))
