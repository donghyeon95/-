
#부분 집합 구하기
def get_subset(string):
    result = []
    if len(string) == 1:
        result.append(string)
        return result
    result = get_subset(string[1:])
    return [string[0]] + [string[0]+result[i] for i in range(len(result))] + result



def solution(orders, course):
    answer = []
    # 후보 메뉴 list
    menu_list = []
    
    for i in orders:
        temp = "".join(sorted(list(i)))
        print(temp)
        menu_list += get_subset(temp)
    
    # 갯수가 정리된 dictionary {메뉴 : 횟수}
    menu_dic = {}
    for menu in menu_list:
        if len(menu) == 1:
            continue
        if menu in menu_dic.keys():
            menu_dic[menu] += 1
        else:
            menu_dic[menu] = 1
    
    print(menu_dic)
    
    keys = menu_dic.keys()
    
    for count in course:
        maximum = 0
        temp = []
        for key in keys:
            if len(key) == count and menu_dic[key] > 1:
                if maximum == menu_dic[key]:
                    temp.append(key)
                elif maximum < menu_dic[key]:
                    temp = []
                    temp.append(key)
                    maximum = menu_dic[key]
        answer += temp
                
    answer.sort()
    
    return answer



# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]