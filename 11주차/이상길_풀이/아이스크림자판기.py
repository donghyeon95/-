def solve():
    n,m = map(int,input().split())

    time = list(map(int,input().split()))
    time = list(enumerate(time,start=1))
    time = sorted(time,key = lambda x:(x[1],x[0]))
    if n > m:
        n = n-m
        cnt = 1
        while True:
            for idx,val in time:
                if cnt%val == 0:
                    n -= 1
                if n == 0:
                    return print(idx)
            cnt += 1
    else:
        for idx, val in time:
            n -= 1
            if n == 0:
                return print(idx)

solve()

                
