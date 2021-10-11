import re

def solution(new_id):
    answer = ''
    
    # 1단계. 소문자 만들기
    answer = new_id.lower()
    
    # 2단계. 특수문자 제거
    #      re.sub('찾을패턴', 바꿀 패턴, '검색할문자열')
    answer = re.sub('[^a-z0-9\_\.\-]+', '', answer)
                  
    # 3단계. 연속한 마침표 제거
    # 이건 틀려서 re.sub씀
    # if '..' in answer:
    #     answer = answer.replace('..', '.')   
    answer = re.sub('\.\.+','.',answer)

    # 4단계. 처음이나 끝에 위치한 마침표 제거
    answer = answer.strip('.')

    # 5단계. 빈 문자열이라면 a 대입
    if answer == '':
        answer = 'a'
    
    # 6단계. 문자열 길이가 16자 이상이라면 처음 15자를 제외한 나머지 제거
    # 마지막 문자가 마침표라면 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    # 7단계. 문자열 길이가 2자 이하라면, 마지막 문자를 길이가 3이될때까지 반복
    while len(answer) < 3:
        answer += answer[-1]

    return answer