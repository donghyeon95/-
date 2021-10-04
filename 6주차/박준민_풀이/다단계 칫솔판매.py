def solution(enroll, referral, seller, amount):
    answer = [0 for x in range(len(enroll))]
    # {"john":0,"mary":1,"edward":2,"sam":3,"emily":4,"jaimie":5,"tod":6,"young":7}
    location_dict = dict(zip(enroll, range(len(enroll))))

    for i in range(len(seller)):
        #처음 판매한 사람
        man = seller[i]
        #처음 판매 금액
        money = amount[i] * 100


        # 상위 판매자가 없을 때 까지 반복
        while man != '-':
            # 처음 판매한 사람의 위치 값 저장
            loc = location_dict[man]
            # parent로 전달할 금액 저장
            div = money // 10

            # 10%를 뺀 나머지 금액 저장
            answer[loc] += money - div
            
            #상위 판매자의 현재 수입
            money = div
            # 상위판매자
            man = referral[loc]

            if div == 0:
                break
                
    return answer