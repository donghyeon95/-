'''
문제 : 직각삼각형
카테고리 : #math
'''


def solution(side) -> str:
    hypo, c1, c2 = side[-1], side[0], side[1]

    if hypo**2 != (c1**2 + c2**2):
        return 'triangle'

    return 'rightangle'


if __name__ == "__main__":
    sides = []
    while True:
        temp = input()
        if temp == '0':
            break
        else:
            sides.append(sorted(list(map(int, temp.split()))))

    for side in sides:
        print(solution(side))
