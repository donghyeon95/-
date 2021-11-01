N = int(input())
H = list(map(int, input().split()))

res = 0

while len(H)>0:
    temp = max(H)
    index = H.index(temp)
    
    while True:
        if temp == 0 or len(H) == 0 or index == len(H):
            res += 1
            break
            
        if H[index] == temp:
            del H[index]
            temp -= 1
        else:
            index += 1
            
print(res)