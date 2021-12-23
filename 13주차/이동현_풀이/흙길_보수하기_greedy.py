# if __name__ == "__main__":
    
#     res = 0

#     with open(".input/input.txt", "r") as f:
#         N, L = list(map(int, f.readline().split()))
#         temp = f.readlines()

#         pools = []

#         for line in temp:
#             pools.append(list(map(int,line.split())))

#         pools = sorted(pools, key=lambda pool:pool[0])

#         newstart = 0
#         for pool in pools:
#             start, end = pool
#             if newstart> start:
#                 start = newstart
#                 res -= 1
#             leng = end - start
#             cnt = leng//L
#             newstart = start+cnt*L + L
#             res += cnt+1


#         print(res)

import sys

if __name__ == "__main__":
    
    res = 0
    cnt = 0
    index = 0 
    new_end = 0
    end = 0
    N, L = list(map(int, sys.stdin.readline().split()))
    pools=[]
    for _ in range(N):
        pools.append(list(map(int, sys.stdin.readline().split())))

    pools = sorted(pools, key=lambda pool:pool[0])
    while True:
        start, end = pools[index]
        if new_end > start:
             start = new_end
        
    
    
    print(res)