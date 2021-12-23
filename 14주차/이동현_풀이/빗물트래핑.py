def isUp(num:int, wall:list):
    N = len(wall)-1
    # if num == 0 or num == N:
    #     return False
    if wall[num-1] < wall[num] > wall[num+1]:
        return True
    return False


# def isDown(num:int, wall:list):
#     N = len(wall)
#     # if num == 0 or num == N:
#     #         return False
#     if wall[num-1] > wall[num] < wall[num+1]:
#         return True
#     return False

if __name__ == "__main__":
    with open(".input\input2.txt", "r") as f:
        wall=list(map(int, f.readline().split(",")))
    
    start = 1
    end = 1
    ans = 0 

    while end < len(wall)-2:
        print('start', start)
        if isUp(end, wall):
            end += 1
            while not isUp(end, wall):
                print('end', end)
                end += 1
            print('start, end', start, end)
            calc_wall = min(wall[start], wall[end])
            for i in range(start, end):
                water = calc_wall - wall[i]
                if water > 0:
                    ans += water
            print("ans", ans)
            start = end
        else : 
            end += 1
            print("__")

    print(ans)