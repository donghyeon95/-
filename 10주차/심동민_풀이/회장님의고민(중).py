'''
문제 : 회장님의 고민
카테고리 : #이분탐색
'''


def cal_amount(n: int, requests: list[int], limit: int) -> int:
    """예산 상한액을 적용하였을 때, 최대 예산배정액을 반환하는 함수
    Args:
        n (int): 예산 요청의 수
        requests (list[int]): 예산 요청 리스트
        limit (int): 예산 상한액
    Returns:
        int: 최대 예산배정액
    """
    amount = 0

    for i in range(n):
        amount += min(requests[i], limit)

    return amount


def binary_search(n: int, requests: list[int], start: int, end: int) -> int:
    """예산 상한액을 이분탐색을 통해 주어진 예산내에서 가능한 최대 예산상한액을 반환하는 함수
    Args:
        n (int): 예산 요청의 수
        requests (list[int]): 예산 요청 리스트
        start (int): 시작값
        end (int): 끝값 (예산요청 중 최대값)
    Returns:
        int: 최대 예산상한액
    """
    while start <= end:
        mid = (start+end) // 2

        result = cal_amount(n, requests, mid)

        if result > budget:
            end = mid - 1
        else:
            start = mid + 1

    return end


if __name__ == "__main__":
    n = int(input())
    requests = list(map(int, input().split()))
    budget = int(input())

    requests.sort()

    # 예산이 모두 배정 가능한 경우, 최대상한액은 요청 중 가장 큰 예산요청액
    if sum(requests) <= budget:
        print(max(requests))
    # 배정이 불가능한 경우 이분탐색을 통해 최대 예산상한액을 계산
    else:
        print(binary_search(n, requests, 0, requests[-1]))
