import string

cheeta = input()

alpha = string.ascii_uppercase
cheeta_list = [[float("inf"),float("inf")] for x in range(len(alpha))]
cnt = 0

# 동선이 안겹치는 치타의 경우 들어오는 점 + 나가는점 = 홀수
# 동선이 겹치는 치타의 경우 짝수가 나올것이므로 동선의 합이 짝수인 치타의 수를 구한다.
# ex) A - 0, 4, B - 1, 5 <<< 서로 겹침
# ex) C - 2, 3, D - 6, 7 <<<< 안겹침
for i in range(len(alpha)):
    for j in range(len(cheeta)):
    
        if alpha[i] == cheeta[j]:
            if cheeta_list[i][0] == float("inf"):
            #   치타의 나간 지점
                cheeta_list[i][0] = j
            else:
            #   치타의 돌아온 지점
                cheeta_list[i][1] = j

        

for i in range(len(alpha)):
    for j in range(i+1, len(alpha)):
        # A 치타가 길을 건넜다 돌아올때까지 다른 치타의 동선 확인
        # 다른 치타의 동선 개수가 홀수일 경우 A치타와 다른 치타의 동선은 겹침

        if cheeta[cheeta_list[i][0] + 1:cheeta_list[i][1]].count(alpha[j]) % 2 == 1:
            cnt+=1

print(cnt)
