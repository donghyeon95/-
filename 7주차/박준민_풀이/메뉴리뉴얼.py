from itertools import combinations

def solution(orders, course):
    answer = []
    
    # 모든 메뉴 조합 만들기
    all_orders = []
    for n in course:
        for order in orders:
            for combi in combinations(order, n):
                menu = ''.join(sorted(combi))
                # all_orders에는 ["XY","XZ","YZ","WX","XY","WY","WX","AW","AX","XYZ","WXY","AWX"]가 들어감
                all_orders.append(menu)
                
    
    menu_count = [{} for x in range(len(course))]
    final_menu = []
    for i in range(len(course)):
        for order in all_orders:
            # 각 메뉴 조합들의 개수를 계산해서 같은 갯수끼리 dict 형식으로 저장
            if len(order) == course[i]:
                # menu_count 에는 [{"XY":2,"XZ":1,"YZ":1,"WX":2,"WY":1,"AW":1,"AX":1},{"XYZ":1,"WXY":1,"AWX":1},{}]가 들어감
                if order in menu_count[i]:
                    menu_count[i][order] += 1
                else:
                    menu_count[i][order] = 1
                    
        # 주문 횟수가 2회 이상인 메뉴들 중에서
        # 2개짜리, 3개짜리, 4개짜리 조합된 메뉴의 각각의 숫자가 제일 많은 것을 return  
        for menu in menu_count[i]:
            if max(menu_count[i].values()) > 1:
                if menu_count[i][menu] == max(menu_count[i].values()):
                    final_menu.append(menu)

    answer = sorted(final_menu)
    return answer