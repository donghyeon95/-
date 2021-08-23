# 자연수 n, k 입력받기
n, k = map(int, input().split())

total = 0

# k번씩 곱한 후 더하기
for i in range(1, n+1):
    total += i ** k

print(total % 1000000009)
