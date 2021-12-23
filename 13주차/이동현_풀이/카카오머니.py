# import fractions

# def solution(N, accounts, moneys):
#     gcd = 0
#     temp = 0
#     for a in range(N):
#         if accounts[a] >= 0:
#             temp = moneys[a]
#             continue
#         # M = 잔액 - 이전 잔액(temp) - (출금 액)
#         M = moneys[a] - temp - accounts[a]
#         gcd = fractions.gcd(M, gcd)
#         temp = moneys[a]

#     return gcd


# if __name__ == "__main__":

#     with open(".input/input.txt", "r") as f:
#         N = int(f.readline())
#         account_list = f.readlines()

#     a = []
#     money = []

#     for account in account_list:
#         temp = list(map(int, account.split()))
#         a.append(temp[0])
#         money.append(temp[1])


#     gcd = solution(N, a, money)

#     if gcd == 1:
#         for n in range(N):
#             if a[n]<0 and money[n] != 0:
#                 print(-1)
#     else:
#         print(gcd)

'''
 무지놈이 무지해서 로그가 모순이 될 수 있다고 한다.

 모순이 생기는 지점은 충전을 하지 않아도 될 때, 계산이 틀리다면 모순이 나오게 된다.

 따라서 모자라지 않을 때, 모순점 검사하고
 모자랄 때는 gcd 갱신 하고 
'''


import math

def solution(N, accounts, moneys):
    gcd = 0
    temp = 0

    for a in range(N):
        if accounts[a] >= 0:
            temp = moneys[a]
            continue
        # M = 잔액 - 이전 잔액(temp) - (출금 액)
        M = moneys[a] - temp - accounts[a]

        gcd = math.gcd(M, gcd)
        temp = moneys[a]

    if gcd == 0:
        return 1

    if gcd > 9 * 10**18:
        return -1

    return gcd

def detect(gcd, a, money, N):
    cnt = 0 
    if gcd == 1:
        for n in range(N):
            cnt += 1
            if a[n]<0 and money[n] != 0 and cnt !=1 :
                return -1
            return 1    
    else:
        return(gcd)

if __name__ == "__main__":

  
    
    # N = int(input())
    

    # a = []
    # money = []

    # for account in range(N):
    #     temp = list(map(int, input().split()))
    #     a.append(temp[0])
    #     money.append(temp[1])



    with open(".input/input.txt", "r") as f:
       N = int(f.readline())
       account_list = f.readlines()

    a = []
    money = []

    for account in account_list:
        temp = list(map(int, account.split()))
        a.append(temp[0])
        money.append(temp[1])
    


    gcd = solution(N, a, money)

    print(detect(gcd, a, money, N))
