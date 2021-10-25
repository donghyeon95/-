n = int(input())
seat = list(map(int, input().split()))
s = int(input())

while True:
    flag = False
    i = n-1

    if not s or i == 0:
        break

    for j in range(i):
        if not s:
            break
        if seat[j] < seat[j+1]:
            seat[j], seat[j+1] = seat[j+1], seat[j]
            s -= 1
            flag = True
            break
    if flag == True:
        continue
    i -= 1


# for i in range(n-1, 0, -1):
#     if not s:
#         break

#     for j in range(i):
#         if not s:
#             break
#         if seat[j] < seat[j+1]:
#             seat[j], seat[j+1] = seat[j+1], seat[j]
#             s -= 1


answer = ''
for i in range(n):
    answer += str(seat[i])

print(answer)
