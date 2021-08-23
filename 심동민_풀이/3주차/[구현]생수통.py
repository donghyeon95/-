# 생수통 가격 입력받기
bottle = [int(input()) for i in range(3)]
# 병뚜껑 입력받기
cap = [int(input()) for i in range(2)]

# 최소가 되는 값 출력
print(min(bottle) + min(cap) + 10)
