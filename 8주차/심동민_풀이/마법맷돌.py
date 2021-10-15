s = input()
t = input()


def solution(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return 0

    if not len(t) % len(s):
        return 1
    return 0


print(solution(s, t))
