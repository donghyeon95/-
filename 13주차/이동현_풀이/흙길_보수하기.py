
def left(end, L,checkedList):
    for i in range(L):
        # 이진탐색 구현
        if end-i in checkedList:
            return True
    return False


def right(start, L, checkedList):
    for i in range(L):
        if start+i in checkedList:
            return True
    return False


if __name__ == "__main__":
    
    checkedList = []
    res = 0

    with open(".input/input.txt", "r") as f:
        N, L = list(map(int, f.readline().split()))

        for _ in range(N):
            start, end = list(map(int, f.readline().split()))
            len = end-start
            cnt = len//L
            leng = cnt*L
            if len%L != 0:
                if not left(end-leng, L, checkedList) and not right(start+leng, L, checkedList):
                    cnt += 1

            res += cnt

            # 힙정렬 구현
            checkedList.append(start)
            checkedList.append(end)
    
    # N, L = list(map(int, input().split()))

    # for _ in range(N):
    #     start, end = list(map(int, input().split()))
    #     len = end-start
    #     cnt = len//L
    #     leng = cnt*L
    #     if len%L != 0:
    #         if not left(end-leng, L, checkedList) and not right(start+leng, L, checkedList):
    #             cnt += 1

    #     res += cnt
    #     checkedList.append(start)
    #     checkedList.append(end)

    print(res)