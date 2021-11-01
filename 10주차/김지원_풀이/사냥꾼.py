n = int(input())
h_list = list(map(int,input().split()))

def dp(dp_t):
    if len(dp_t) == 0:
        return 0
    if len(dp_t) == 1:
        return 1
    for i in range(len(dp_t)-1,-1,-1):
        if (dp_t[i] + 1) != dp_t[i-1]:
            return 1 + dp(dp_t[:i])

print(dp(h_list))
