
n= int(input())
if n == 1:
    print(9)
else:
    # 필요한 건 각 숫자의 갯 수이다.
    # index는 숫자를 뜻하고 val는 그 숫자가 몇개 인지이다.
    count_nums = [1]*10
    count_nums[0] = 0

    for _ in range(n-1):
        temp = [0]*10
        for idx,val in enumerate(count_nums):
            if idx == 0:
                temp[idx+1] +=  val
            elif idx == 9:
                temp[idx-1] += val
            else:
                temp[idx+1] += val
                temp[idx-1] += val
            count_nums = temp
    print(sum(count_nums)%1000000000)        



