def solution(lottos, win_nums):
    answer = []
    num = 0
    mis = 0
    for i in range(6):
        if lottos[i] == 0:
            mis += 1
            continue
            
        for j in range(6):
            if (lottos[i] == win_nums[j]):  
                num += 1
    if mis == 6:
        answer = (1,6)           
    elif num == 0:
        answer = (6, 6-mis)

    else :
        answer = (7-num-mis, 7-num)
         
    return answer
