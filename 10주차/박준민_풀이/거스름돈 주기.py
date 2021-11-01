from itertools import combinations

n = int(input())
c = list(map(int, input().split()))
m = int(input())

# c.sort(reverse=True)
coin_list = []
for i in range(1, n + 1):
    coin_list.append(combinations(c, i))
    
cnt = 0
# c_sum = 0
for i in coin_list:
    for j in list(i):
        # print(j)
        c_sum = 0
        for k in range(len(j)):
            c_sum += j[k]
            
        
        if c_sum < m:
            for l in range(len(j)):
                # print(j[l])
                while c_sum < m:
                    # print(j[l])
                    c_sum += j[l]
                # print(c_sum, j[l])

        
        if c_sum == m:
            cnt +=1
        # print(c_sum, cnt)
        # print()
print(cnt)