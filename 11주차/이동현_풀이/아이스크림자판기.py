# if __name__ == "__main__":
#     N, M = list(map(int, input().split()))
#     time_list = list(map(float, input().split()))

'''
시간을 반복해서 곱했을 때 정수라면 N+1을 해준다. 

시간 초과인듯 : 60점

'''   
#     if N <= M:
#         print(N)
    
#     else:
        
#         cal_time_list = list(map(lambda i: i**-1, time_list))
#         # float.is_integer()를 사용해서 정수인 값만 sum을 할 것이다.
        
#         i = 1
#         flag = 0
#         result = M
        
#         while True:
            
#             # print(result)
#             if i == 20:
#                 break
#             temp_list = list(map(lambda x: x * i, cal_time_list))
#             # print(temp_list)
#             for time_index in range(len(temp_list)):
#                 if temp_list[time_index].is_integer():
#                     # print(temp_list[time_index])
#                     result += 1
#                     if int(result) == N:
#                         # print(result)
#                         print(time_index+1)
#                         flag = 1
#                         break
                        
#             if flag == 1:
#                 break
                
#             i += 1

'''
time은 현재 시간 
res는 이용한 병정 수
얘도 시간 초과인 듯 하다. 
'''

def factor(time, res, N, M):
    for i in range(1, M+1):
        if time%i == 0:
            # print(res)
            # print("time",time)
            res += 1
        if res == N:
            return i, res, 1

    return 0, res, 0
        

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    time_list = list(map(float, input().split()))
    

    if N <= M:
        print(N)
    
    else:
        result = 5
        time = 1
        while True:
            if time == 30:
                break
            
            index, res, flag = factor(time, result, N, M)
            
            
            if flag == 1:
                print(index)
                break
                
            result = res
            # print(time, result)
            time += 1
            






