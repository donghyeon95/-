n = int(input())
budget = list(map(int, input().split()))
m = int(input())


first, last = 0, max(budget)
while first <= last:
    mid = (first + last) // 2
    
    cost = 0
    for i in budget:
        cost += min(i, mid) 
    
    if cost > m:
        last = mid - 1
    else :
        first = mid + 1
        
    # print(cost, mid, first, last)
    # elif로 할 경우 2번케이스 시간초과
    # elif cost < m:
    #     first = mid + 1

print(last)


# 4번 케이스 시간 초과
# while(sum(budget) >= m):
#     if budget[0] != max(budget):
#         budget.sort(reverse = True)
    
#     # print(budget)
#     budget[0] -= 1

#     if sum(budget) < m:
#         break
        
# print(max(budget))


