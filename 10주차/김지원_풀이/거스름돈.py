n = int(input())
coins = list(map(int,input().split()))
money = int(input())

dp = [1]+[0]*money


for coin in coins:
    for price in range(coin, money+1):
        if price >= coin:
            dp[price] += dp[price-coin]
            
print(dp[money])