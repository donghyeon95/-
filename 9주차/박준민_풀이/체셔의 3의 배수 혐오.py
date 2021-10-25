n = int(input())
num = list(map(int, input().split()))

num_list = []
phobia = 0
temp = 0

for i in range(len(num) -1):
    phobia = num[i] + num[i+1]
    if phobia % 3:
        temp = num[i]
        num[i] = num[i+1]
        num[i+1] = temp
        
        
print(*(num))