n = int(input())
array = list(map(int, input().split()))


def solution(n, array):
    idx = 0
    while True:

        if idx+2 >= n:
            if not (array[idx] + array[idx+1]) % 3:
                return -1
            return array

        if not (array[idx] + array[idx+1]) % 3:
            array[idx+1], array[idx+2] = array[idx+2], array[idx+1]
        idx += 1


print(solution(n, array))
