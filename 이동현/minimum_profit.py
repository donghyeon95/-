def insert(link):  
    parent, children = link
    tree[parent][2].append(children)
    tree[parent][3] = min(tree[children][1], tree[parent][3])

def dfs(child, result_min, pre_min):
    '''
    if Leaf 노드이면 return result_min
    result_min += min ((result_min + tree[child] [3]), (result_min - pre_min, tree[child] [0])
    for nex in tree[child]:
        result_min = dfs(nex, result_min, pre_min)
    return result_min
    '''
    print(child, result_min, pre_min)
    node = tree[child]
    if len(node[2]) == 0:
        # print(result_min)
        return result_min
    # 최소값을 선택 된 놈으로 갱신해줄 필요가 있다(이전에 선택된값으로 갱신해주어야 한다??.)
    if result_min+node[3] < result_min - pre_min + node[1]:
        result_min = result_min+node[3]
        temp = node[3]
    else:
        temp = node[1]
        result_min = result_min - pre_min + node[1]
    for nex in node[2]:
        result_min = dfs(nex, result_min, temp)
    return result_min

def solution(sales, links):
    answer = 0
    N = len(sales)
    #tree에 튜플 형태로 집어 넣는 다. 
    # (자신의 번호, 자신의 가격, chidren_list, 자신과 자식들 중 최소(처음에는 자기자신을 넣어야).)
    global tree
    tree = [[i,sales[i-1],[],sales[i-1]] for i in range(1, N+1)]
    tree.insert(0,0)
    
    for link in links:
        insert(link)
    #check리스트를 따로 만든다. 
    # check = [False for i in range(N+1)]
    print(tree)
    answer = tree[1][3]
    for i in tree[1][2]:
        answer = dfs(i, answer, tree[1][3])
    
    
    return answer
    

# print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))


'''
최대 최소 문제이기 때문에 DP를 사용해야 할 듯.



1.가장 먼저 드는 생각은  
    a. A의 최소() + B의 최소(같은 놈일 경우, b로 ) 
    
        만약 최소값을 가진 친구가 여러개 있다면 뭐를 선택해야 한다?
            우선순위 루트 -> 자식이 있는 친구(여기서의 우선 순위는?) -> 자식이 없는...인가??
            걍 전체의 최소로 하면 노상관인듯.. 아마도..?????
    
        a-1 이미 선택이 되어 있다면
            (선택 되어 있는 것은, b의 최소 or a와b의 겹친놈..)
            상위 부서가 이전 작업을 한 놈과 겹쳐 있는 놈이면서 겹치는 놈을 선택해야 할 때,
            의 최소 값을 구하면 된다. 
    b. 둘이 겹쳐 있는 놈
            
    dfs를 하는 데 LeaF 전까지..
    자료 구조는 튜플로 하고, 
    각 루트는 자기와 자기 자식들 중 최소 값을 가지고 있도록 입력을 해주면 될 듯.
    부모로 부터 이전의 최소값도 가지고 있어야 할 듯.
    
    
    
    min(a,b)를 선택하는 것.
    
    근데 이게 확실히 정답을 보장하나?
'''
