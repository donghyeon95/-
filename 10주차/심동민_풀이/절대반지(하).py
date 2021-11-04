'''
문제 : 절대반지
카테고리 : #string
'''


if __name__ == "__main__":
    nickname = input()
    numOfRing = int(input())

    answer = 0

    for _ in range(numOfRing):
        if nickname in input()*2:
            answer += 1

    print(answer)
