
def solution(index, S):
    A = arr[index]
    max_num = [0,0]
    
    for i in range(index, len(arr)):
        if S < i-index:
            break
        if max_num[0] < arr[i]:
            max_num[0] = arr[i]
            max_num[1] = i
            
    return max_num
            


input()

arr = list(map(int, input().split()))
S = int(input())

index = 0

while True:
    if S == 0 or index == len(arr):
        break
    Num, idx = solution(index, S)
    
    temp = arr[idx] 
    arr[idx] = arr[index]
    arr[index] = temp 
    
    
    S -= (idx-index)
    index = index + 1


print("".join(map(str,arr)))