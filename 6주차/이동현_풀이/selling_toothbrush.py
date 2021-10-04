
import math
#이익금을 부모에게 재분배 하는 함수
# def reverse(enroll, referral, node, profit, answer):
#     #종료 조건 : 더이상 나에게 부모가 없을 경우 + 받은 금액이 10미만일 때,
#     idx = enroll.index(node)
#     if node == "-" :
#         return 
#     if profit<10:
#         answer[idx] += profit
#         return 0
    
#     if referral[idx]=="-" :
#         answer[idx] +=  math.ceil(profit * 0.9)
#         return 0
#     else:
#         parent = referral[idx]
#         a = math.ceil(profit * 0.9)
#         answer[idx] += a
#         reverse(enroll, referral, parent, math.floor(profit * 0.1) , answer)

# def solution(enroll, referral, seller, amount):
#     answer = [0 for i in range(len(enroll))]
    
#     for idx in range(len(enroll)):
#         #부모가 없을 경우
#         if referral[idx] == "-":
#             # 내가 수익을 낸 경우
#             if enroll[idx] in seller:
#                     i = seller.index(enroll[idx])
#                     answer[idx] += amount[i] * 90
#         #부모가 있을 경우
#         else:
#             parent = referral[idx]
#             print(parent)
#             #내가 수익을 낸 경우
#             if enroll[idx] in seller:
#                     #나는 0.9만큼을 가지고
#                     i = seller.index(enroll[idx])
#                     answer[idx] += amount[i] * 90
#                     # 0.1을 부모에게 reverse 한다. 
#                     reverse(enroll, referral, parent ,amount[i]*10, answer)
    
#     return answer


#아마 매번 find를 해야 되서 시간이 많이 들었던 것 같음. 
# 딕셔너리에 저장을 하든, 리스트에 튜플로 저장하든 부모 정보를 미리 저장해야 할 듯. 
#반복문을 seller만 해서 돌리자. 

# 오답은 왜 나오는 지 모르겠다. 


def reverse(enroll, referral, node, profit, answer):
    #종료 조건 : 더이상 나에게 부모가 없을 경우 + 받은 금액이 10미만일 때,
    if node == "-" :
        return 0
    
    idx = enroll.index(node)

    if profit<10:
        answer[idx] += profit
        return 0
    
    if referral[idx]=="-" :
        answer[idx] +=  math.ceil(profit * 0.9)
        return 0
    else:
        parent = referral[idx]
        a = math.ceil(profit * 0.9)
        answer[idx] += a
        reverse(enroll, referral, parent, profit-a, answer)

def solution(enroll, referral, seller, amount):
    answer = [0 for i in range(len(enroll))]
    
    for idx in range(len(seller)):
        enroll_idx = enroll.index(seller[idx])
        parent = referral[enroll_idx]

        #나는 0.9만큼을 가지고
        answer[enroll_idx] += amount[idx] * 90
        # 0.1을 부모에게 reverse 한다. 
        reverse(enroll, referral, parent ,amount[idx]*10, answer)
    
    return answer

#정답은 다 나오는 거 같은데, seller로 반복문 돌려도 시간을 안 줄어듦.
#호출 횟수를 줄여야 되는 거 같은데, 어떤 자료구조로 만들어야 하나??
