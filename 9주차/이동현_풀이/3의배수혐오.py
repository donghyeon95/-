# def istriple(num1, num2):
#     if (num1 + num2) % 3 == 0:
#         return True
#     else: 
#         return False
        
        
# def solution(N, arr):
#     # print(arr)
#     if len(arr) == 1:
#         return " ".join(map(str,arr))

#     for index in range(len(arr)-1):
                
#         if istriple(arr[index], arr[index+1]):
#             i = 1
#             while True:
#                 if index+i == len(arr):
#                     return -1

#                 if not istriple(arr[index], arr[index+i]):
#                     temp = arr[index+1]
#                     arr[index+1] = arr[index+i]
#                     arr[index+i] = temp
#                     break
                    
#                 else:
#                     i += 1
                    
#     return " ".join(map(str,arr))

# def revers(N, arr):
#     # print(arr)
#     if len(arr) == 1:
#         return " ".join(map(str,arr))

#     for index in reversed(range(len(arr))):
#         if index == 0:
#             break

#         if istriple(arr[index], arr[index-1]):
#             i = 1
#             while True:
#                 if index-i == -1:
#                     return -1

#                 if not istriple(arr[index], arr[index-i]):
#                     temp = arr[index-1]
#                     arr[index-1] = arr[index-i]
#                     arr[index-i] = temp
#                     break
                    
#                 else:
#                     i += 1
                    
#     return " ".join(map(str,arr))    


# N = int(input())
# arr = list(map(int, input().split()))

# arr.sort()
# # print(solution(N,arr))
# K = solution(N,arr)

# if K == -1:
#     print(revers(N, arr))
    
# else:
#     print(K)


input()
a=[[],[],[]]
for v in map(int,input().split()):a[v%3]+=v,
if len(a[0])>1+len(a[1]+a[2])or (a[1] and a[2] and not a[0]):print(-1)
else:
 r=[]
 for v in a[0]:
  if r:r+=(a[1]or a[2]).pop(),
  r+=v,
  print(a[1],a[2], r),
 print(*a[1]+r+a[2])

