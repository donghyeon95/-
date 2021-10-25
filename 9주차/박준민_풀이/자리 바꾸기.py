# 한번 바꿈
# 20, 10, 30, 40, 50, 60, 70
# 두번 바꿈
# 20, 30, 10, 40, 50, 60, 70
# 세번 바꿈
# 30, 20, 10, 40, 50, 60, 70

#설명하기가 애매....

def get_list(seat, s):
    res = ""
    
    # s번 만큼 반복
    for i in range(s):
        num_list = change_num(seat)

    #출력처리
    for i in num_list:
        res += str(i)
        
    print(res)


# 무조건 seat[0]부터 비교해서 정렬
def change_num(seat):
    
    for i in range(len(seat) - 1):
        if seat[i] < seat[i + 1]:
            temp = seat[i]
            seat[i] = seat[i + 1]
            seat[i + 1] = temp

            return seat

    # 더이상 정렬할게 없을경우
    return seat
    
n = int(input())
seat = list(map(int, input().split()))
s = int(input())


get_list(seat, s)
