n = int(input())
n_list = list(map(int,input().split()))
m = int(input())

def b_search(data,m):
    data.sort()
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_temp = m // (len(data) - (start))
        if data[mid] <= mid_temp:
            m -= sum(data[start:mid+1])
            start = mid + 1
        else:
            end = mid - 1
    if start == len(data):
        return data[-1]
    else:
        return m // (len(data) - (start))

print(b_search(n_list,m))