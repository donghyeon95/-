import collections
from typing import Counter


def solution(strs: str) -> int:
    count = 0
    stack = []

    for string in strs:
        if len(stack) < 1:
            stack.append(string)
            continue

        if stack[-1] != string:
            stack.append(string)
        else:
            stack.pop()
            continue

    if len(stack) <= 1:
        return count

    result = collections.Counter(stack)
    result = len(result.keys())

    for i in range(result):
        count += i

    return count


def main():
    strs = input()

    print(solution(strs))


if __name__ == '__main__':
    main()
