#효율성 0점ㅋ
def solution(info, query):
    answer = [0 for i in range(len(query))]
    info_list = []
    query_list = []

    # info 분리
    for i in info:
        info_list.append(i.split())
    
    # query 분리
    for q in query:
        temp_q = q.split()
        # split() 후, list에서 and 제거
        while len(temp_q) > 5:
            temp_q.remove('and')
        query_list.append(temp_q)

    # info_list[i]와 query_list[q]를 비교
    for i in range(len(info_list)):
        for q in range(len(query_list)):
            
            # 비교할 조건은 5개
            for n in range(5):
                # query_list가 상관없음('-')이면 continue
                if query_list[q][n] == '-':
                    continue
                    
                # 코딩테스트 점수 비교
                elif n == 4:
                    if int(info_list[i][n])>= int(query_list[q][n]):
                        answer[q] += 1
                        
                # 조건이 맞지 않을 때
                elif info_list[i][n] != query_list[q][n]:
                    break
    
    return answer