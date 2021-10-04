def solution(lottos, win_nums):
    answer = []
    l_cnt =  0 #일치한 번호
    z_cnt = lottos.count(0) #알아볼 수 없는 번호
    rank = [6, 6, 5, 4, 3, 2, 1] # 로또 등수
    #   0 <= l_cnt <= 6, 0 <= z_cnt <= 6
    #   z_cnt가 6일 경우, max_rank는 rank[6], min_rank[0]을 가져와야하기 때문에
    #   rank[0]에 6을 한번 더 집어넣음

    for l in lottos:
            if l in win_nums:
                    l_cnt +=1
                    
    max_rank = rank[l_cnt + z_cnt] #최고 등수
    min_rank = rank[l_cnt]  #최저 등수
    answer = [max_rank, min_rank]
    
    return answer

# 아래 코드는 테스트 14번을 통과하지 못함
# def solution(lottos, win_nums):
#     answer = []
#     l_cnt = 0
#     z_cnt = lottos.count(0)
    
#     for l in lottos:
#             if l in win_nums:
#                 l_cnt +=1
    
#     max_rank = 7 - (l_cnt + z_cnt)
    
#     if z_cnt == 6:
#         min_rank = 6
#     else:
#         min_rank = 7 - l_cnt
        
#     answer = [max_rank, min_rank]
#     return answer