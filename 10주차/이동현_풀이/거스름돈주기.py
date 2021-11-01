def HowMuch(change):
    result = 0
    if change == 0:
        return 1
    if memo[change] is not 0:
        return 0
    for K in CN:
        if K > change:
            continue
        result += HowMuch(change-K)
    memo[change] += result
    print(result, change)
    return result

N = int(input())
global CN
CN = list(map(int, input().split()))
M = int(input())
print(CN)
global memo
memo = [0 for i in range(M)]
result = 0


for i in range(N):
    result += HowMuch(100-CN[i])
    
print(result)