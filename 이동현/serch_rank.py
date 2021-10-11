
from enum import Enum
import copy

class Lang(Enum):
    python = 0
    java = 1
    cpp = 2
    
class Skill(Enum):
    backend = 0
    frontend = 1

class career(Enum):
    junior = 0
    senior = 1

class menu(Enum):
    chicken = 0
    pizza = 1


def make(instance, num_list): 
    cnt = num_list[0]
    for i in range(cnt):
        instance.append(list())
        if len(num_list) > 2:
            make(instance[i], num_list[1:])
            
def return_query(query):
    l = query.split(" and ")
    y = l[-1].split(" ")
    menu = y[0]
    score = y[1]
    del l[-1]
    l.append(menu)
    l.append(score)
    return l
    

def insert(info, tree):
    if len(info) == 1:
        tree.append(info[0])
        return 
    nex = info.pop(0)
    clas = leng[4-len(info)]
    insert(info, tree[clas[nex].value])
        

def search(query, tree):

    # print(tree)
    if len(query) == 1:
        cnt = 0 
        num = query[0]
        for i in tree:
            # print("i",i, "num", num)
            if type(i) == str and int(i)>= int(num):
                cnt +=1
        return cnt
    else:
        nex = query.pop(0)
        clas = leng[4-len(query)]
        cnt = 0
        if nex == "-":
            for i in tree:
                a = copy.deepcopy(query)
                # print(len(a),"tree",i)
                
                cnt += search(a, i)
            return cnt
        else:
            return search(query, tree[clas[nex].value])
        
        


def solution(info, query):
    answer = []
    tree = []
    global leng 
    leng = [Lang, Skill, career, menu]
    #만들 공간 리스트
    num_list = [3,2,2,2,1]
    make(tree, num_list)
    # for lang in tree:
    #     for skill in lang:
    #         for ca in skill:
    #             for me in ca:
    #                 for i in me:
    #                     print(i)
    query_list = []
    
    for i in info:
        insert(i.split(" "), tree)
    # for lang in tree:
    #  for skill in lang:
    #     for ca in skill:
    #         for me in ca:
    #                 print(me)
    for i in query:
        query_list.append(return_query(i))
    for query in query_list:    
        answer.append(search(query, tree))
        # print(answer)
    
    return answer





# from enum import Enum
# import copy

# class Lang(Enum):
#     python = 0
#     java = 1
#     cpp = 2
    
# class Skill(Enum):
#     backend = 0
#     frontend = 1

# class career(Enum):
#     senior = 0
#     junior = 1


# class menu(Enum):
#     chicken = 0
#     pizza = 1


# def return_query(query):
#     l = query.split(" and ")
#     y = l[-1].split(" ")
#     menu = y[0]
#     score = y[1]
#     del l[-1]
#     l.append(menu)
#     l.append(score)
#     return l
    

# def insert(info, index):
#     if len(info) ==  1:
#         tree[index].append(info[0])
#         return
#     a = info.pop(0)
#     index = 2*index + enum[len(info)-1][a].value
#     insert(info, index)
    
    
# def search(query, index, n):
#     cnt = 0

#     if n == 4:
#         num = int(query[n])
#         # print(num)
#         # print("last",index)
#         # print(query, tree[index])
#         for i in tree[index]:
#             if int(i) >= num:
#                 # print("i",i)
#                 cnt += 1
#         # print("cnt",cnt)
#         return cnt

#     if query[n] == "-":
#         for i, _ in enumerate(enum[3-n]):
#             # print(query,enum[3-n], cnt,i )
#             cnt += search(query, 2*index + i, n+1)
            
#         return cnt
#     else:
#         index = 2*index + enum[3-n][query[n]].value
#         return search(query, index, n+1)

# def solution(info, query):
#     answer = []
#     global tree
#     tree = [[] for i in range(24)]
#     global enum 
#     enum = [menu, career, Skill, Lang]
#     query_list = []
    
#     for i in query:
#         query_list.append(return_query(i))
        
#     for i in info:
#         insert(i.split(" "), 0)
#     # print(tree)
#     for q in query_list:
#         answer.append(search(q, 0, 0))
#     # print(answer)
#     return answer
