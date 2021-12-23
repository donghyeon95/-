

if __name__ == "__main__":
    with open(".input\input4.txt", "r") as f:
        num = list(map(int, f.readline().split()))

    num.sort()
    ans = 0

    for i in range(0, len(num), 2):
        ans += num[i]
    
    print(ans)