# 시간 입력받기
time = [int(input()) for _ in range(4)]

# 총 시간을 60으로 나누어 분, 초로 계산
minute, sec = divmod(sum(time), 60)

print(minute, sec, sep='\n')
