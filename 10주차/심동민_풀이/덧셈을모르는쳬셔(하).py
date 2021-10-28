'''
문제 : 덧셈을 모르는 쳬셔
카테고리 : #math
'''


def solution(nums):
    total = 0
    temp = ''

    for num in nums[::-1]:
        if num == '0':
            temp += num
            continue

        temp = num + temp
        total += int(temp)
        temp = ''

    return total


if __name__ == "__main__":
    nums = input()

    print(solution(nums))
