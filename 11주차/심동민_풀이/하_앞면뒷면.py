'''
문제 : 앞면 뒷면
카테고리 : 수학
'''

n = int(input())
answer = 1
now, interval = 1, 3

while True:
    now += interval
    interval += 2

    if now > n:
        break
    answer += 1


print(answer)
