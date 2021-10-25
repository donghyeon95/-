def linearNum(numList, length):
    result = []
    
    cnt = 0
    
    temp = [0]
    
    for i in numList:
        temp2 = list(map(lambda x: x+i , temp))
        temp = [0] + temp2
        result += temp2
            
    return result
    

def binarySearch(Nlist, num, T):
    
    if len(Nlist) == 1:
        return 0
    
    mid = len(Nlist)//2
    
    S = Nlist[mid] + num 
    
    if S == T:
        return Nlist.count(Nlist[mid])
        
    if S > T:
        return binarySearch(Nlist[:mid], num, T)
    else:
        return binarySearch(Nlist[mid:], num, T)
    
    
f = open('9주차\이동현_풀이\input.txt', 'r')


T = int(f.readline())

LA = int(f.readline())
A = list(map(int, f.readline().split()))

LB = int(f.readline())
B = list(map(int, f.readline().split()))


#순서 쌍
AList = sorted(linearNum(A, LA))
BList = sorted(linearNum(B, LB))
print("A :", AList, "\nB:", BList)

res = 0

for B in BList:
    res += binarySearch(AList, B, T)    
    print("res :", res, ", B: ", B)
    
print(res)

f.close()
