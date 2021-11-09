N = int(input())

temp = [1] * 10 + [0]
result = [0] * 9



for i in range(N-1):
    for j in range(9):
        result[j] = temp[j]+temp[j+2]
    temp = [temp[1]] + result + [0]

if N==1:
    print(9)
else:
    print(sum(result)%1000000000)