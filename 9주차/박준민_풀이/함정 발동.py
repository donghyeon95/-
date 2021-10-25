room = []

for i in range(8):
    room.append(input())
    
cnt = 0

for i in range(len(room)):
    for j in range(len(room[i])):
        if i % 2 == 0 and j % 2 == 0 and room[i][j] == 'H':
            cnt += 1 
        elif i % 2 != 0 and j % 2 != 0 and room[i][j] == 'H':
            cnt += 1
                
print(cnt)