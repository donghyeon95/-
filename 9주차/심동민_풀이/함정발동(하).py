ans = 0


def solution(idx, array):
    man = 0

    if idx % 2:
        for i, elem in enumerate(array):
            if i % 2 and elem == 'H':
                man += 1
    else:
        for i, elem in enumerate(array):
            if not (i % 2) and elem == 'H':
                man += 1

    return man


for idx in range(8):
    ans += solution(idx, list(input()))

print(ans)
