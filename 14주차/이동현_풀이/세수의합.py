

if __name__ == "__main__":
    with open(".input\input3.txt", "r") as f:
        num = list(map(int, f.readline().split()))

    num.sort()
    ans = []

    for i in range(len(num)-2):
        if i > 0 and num[i] == num[i-1]:
            continue
        for j in range(i+1, len(num)-1):
            if j > i+1 and num[j] == num[j-1]:
                continue
            for k in range(j+1, len(num)):
                if k > j+1 and num[k] == num[k-1]:
                    continue
                if num[i]+num[j]+num[k] == 0:
                    ans.append([num[i], num[j], num[k]])

    print(ans)