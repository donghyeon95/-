n = int(input())
array = list(map(int, input().split()))


def solution(n, array):
    idx = 0
    while True:

        if idx+2 >= n:
            if not (array[idx] + array[idx+1]) % 3:
                return -1
            return array

        if not (array[idx] + array[idx+1]) % 3:
            array[idx+1], array[idx+2] = array[idx+2], array[idx+1]
        idx += 1


print(solution(n, array))





# 모범 답안
input()
a=[[],[],[]]
for v in map(int,input().split()):a[v%3]+=v,
if len(a[0])>1+len(a[1]+a[2])or (a[1] and a[2] and not a[0]):print(-1)
else:
 r=[]
 for v in a[0]:
  if r:r+=(a[1]or a[2]).pop(),
  r+=v,
 print(*a[1]+r+a[2])
