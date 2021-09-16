n = int(input())
sauce = list(map(int, input().split()))

candi_list = []

least = 1000001

# 브루트 포스
for i in range(len(sauce) + 1):
    for j in range(i+1, len(sauce)):
        if abs(sauce[i] + sauce[j]) < least:
            least = abs(sauce[i] + sauce[j])
            candi_list.append((abs(sauce[i] + sauce[j]), sauce[i], sauce[j]))


candi_list.sort(key=lambda x: x[0])

print(candi_list[0][1], candi_list[0][2])
