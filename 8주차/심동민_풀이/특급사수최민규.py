n = int(input())


def getDivisor(n):
    count = 0
    for i in range(1, n+1):
        if not n % i:
            count += 1

    return count


stage = 1

while True:
    score = (stage * (stage + 1)) // 2

    div = getDivisor(score)

    if n < div:
        break

    stage += 1

print(score)
