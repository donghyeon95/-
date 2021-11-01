def shoot(s_position, h_list, start):
    # 거미를 맞출때마다 높이를 1씩 낮추기 위한 변수 선언
    s_height = s_position[start]
    
    for i in range(start, len(s_position)):
        # 높이가 0이되면 return
        if s_height == 0:
            return h_list
        
        # 현재 총알의 높이와 거미의 높이가 같다면 현재 위치의 hit_list를 +1해주고 총알의 높이를 -1해준다
        if s_height == s_position[i]:
            h_list[i] += 1
            s_height -= 1
            
        # print(s_height, h[i], h_list)

    
n = int(input())
h = list(map(int, input().split()))

cnt = 0 # 필요한 총알 개수
hit_list = [0 for _ in range(len(h))] # 맞춘 거미의 위치 표시하기위한 list
start_point = 0 # 총알을 쏘는 지점

while True:
    shoot(h, hit_list, start_point)

    # 0이 나오는 최초의 지점에서 다시 총을 쏘기위한 처리
    for i in range(len(hit_list)):
        if hit_list[i] == 0:
            start_point = i
            break
    
    cnt += 1

    # 모든 거미를 맞췄으면 return
    if 0 not in hit_list:
        break
        

print(cnt)
