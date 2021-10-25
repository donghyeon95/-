# a, b 각각 t보다 작은 연속된 숫자의 합을 구해서 list로 저장
#num = a, b, length = n, m
def get_num_list(num, length):
    num_list = num
    c_num = 0
    # a가 n개일때 연속된 숫자의 합을 구함
    # ex) 1+3, 3+1, 1+2, 1+3+1, 3+1+2, 1+3+1+2
    # i는 연속적인 구간의 갯수, j는 시작지점, k는 시작지점부터 i개만큼 더한 값을 계산
    for i in range(2, length+1):
        for j in range(length-i+1):
            # print(i, j, num[j])
            for k in range(j, j+i):
                c_num += num[k]
                
                if c_num >= t:
                    continue

            # a_num이 t보다 클 경우 
            if c_num < t:
                num_list.append(c_num)
            else:
                continue
            c_num = 0
            
    return num_list

# a와 b 리스트를 각각 비교해서 t가 나오는 횟수를 계산
def add_num(a, b):
    cnt = 0
    for i in a:
        for j in b:
            # print(i, j)
            if i + j == t:
                
                cnt += 1
    return cnt

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


a_list = get_num_list(a, n) # [1, 3, 1, 2, 4, 4, 3]
b_list = get_num_list(b, m) # [1, 3, 2, 4]

# print(a_list, b_list)


print(add_num(a_list, b_list))

# print(add_num(a, b), add_num(a_list, b_list), add_num(a, b_list), add_num(b, a_list))
# print(add_num(a, b_list) + add_num(b, a_list))
# print(add_num(b, a_list))


######## 아래만 해도 60점
# def add_num(a, b):
#     cnt = 0
#     for i in a:
#         for j in b:
#             if i + j == t:
#                 cnt += 1
#     return cnt
    
# a_list = []
# for i in range(n-1):
#     a_list.append(a[i] + a[i+1])


# b_list = []
# for i in range(m-1):
#     b_list.append(b[i] + b[i+1])

# count = add_num(a, b) + add_num(a, b_list) + add_num(b, a_list)
# print(count)