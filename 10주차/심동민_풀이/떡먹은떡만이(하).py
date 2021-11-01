'''
문제 : 떡 먹은 떡만이
카테고리 : #simulation
'''


def solution(m: int, change_pos: list[list]):
    answer = 1

    for pos in change_pos:
        if answer in pos:
            pos.remove(answer)
            answer = pos.pop()

    return answer


if __name__ == "__main__":
    m = int(input())
    change_pos = []

    for _ in range(m):
        change_pos.append(list(map(int, input().split())))

    print(solution(m, change_pos))
