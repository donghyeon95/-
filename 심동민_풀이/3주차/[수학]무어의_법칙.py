# 자연수 입력받기
n = int(input())

num, answer = 2 ** n, 0

# 10으로 나눈 나머지 값으로 각 자릿수 더하기
while num != 0:
    a, b = divmod(num, 10)
    answer += b
    num = a

print(answer)
