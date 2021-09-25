# A가 퇴사 했을 때, B가 A의 업무를 떠맡고(10 + 20), C가 퇴사해서 B가 그 일을 떠맡는다면(30(10 + 20) + 40)
# A가 퇴사 했을 때, C가 A의 업무를 떠맡고(10 + 40), C가 퇴사해서 B가 그 일을 떠맡는다면(50(10 + 40) + 20)
# 따라서 업무량이 제일 작은사람이 퇴사자의 업무를 떠맡는다.
# 업무량이 제일 작은 사람순으로 퇴사
n = int(input())

work = []

for i in range(n):
    work.append(int(input()))
    

res = 0
while len(work) > 1:
    # 가장 작은 값 기준으로 정렬
    work.sort()
    
    # 가장 작은 값을 저장할 변수
    min_work = work[0]
    # 가장 작은 값 제거 (A의 업무 10)
    work.remove(work[0])

    # 두번째로 작은 값에 제거했던 가장 작은 값 추가 (B에게 A의 업무 할당)
    work[0] = work[0] + min_work

    # 업무량 총합 계산
    res += work[0]

print(res)

