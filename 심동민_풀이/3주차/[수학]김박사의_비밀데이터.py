# 데이터 개수 입력받기
n = int(input())

# 체크 암호 초기값
check_password = 0

# 데이터 개수만큼 데이터 입력받기
for _ in range(n):
    check_password += int(input())

# 앞에서부터 10자리수 출력
print(str(check_password)[0:10])
