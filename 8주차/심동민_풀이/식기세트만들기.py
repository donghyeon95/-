c, s, e = map(int, input().split())

set_count = 0
remain = c + s

while remain - e >= 3:
    if c >= 2:
        c -= 2
    else:
        break

    if s > 0:
        s -= 1
    else:
        break

    set_count += 1

    remain = c + s


print(set_count)
