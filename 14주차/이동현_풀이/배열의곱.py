

if __name__ == "__main__":
    with open(".input\input5.txt", "r") as f:
        num = list(map(int, f.readline().split()))

    left = [1]
    right = [1]
    
    ans = []

    for i in range(len(num)):
        left.append(left[i]*num[i])

    left.append(1)

    for i in range(len(num)-1, -1, -1):
        right.insert(0, right[0]*num[i])
    
    right.insert(0, 1)

    for i in range(len(num)):
        ans.append(left[i]*right[i+2])

    print(ans)