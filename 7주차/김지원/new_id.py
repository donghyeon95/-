def solution(new_id):
    new_id = new_id.lower()
    new_id1 = []
    char =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','.','-','_']
    for i in new_id:
        if i in char:
            if len(new_id1) >= 1 and i == '.':
                if new_id1[-1] == '.':
                    continue
            new_id1.append(i)
    if len(new_id1) < 2:
        if new_id1[-1] == '.':
            new_id1.pop()
    else:
        if new_id1[0] == '.':
            new_id1.pop(0)
        if new_id1[-1] == '.':
            new_id1.pop()
    if len(new_id1) == 0:
        new_id1.append('a')
    if len(new_id1) > 15:
        new_id1= new_id1[:15]
        if new_id1[-1] == '.':
            new_id1.pop()
    if len(new_id1) <= 2:
        for i in range(3-len(new_id1)):
            new_id1.append(new_id1[-1])
    new_id1 = ''.join(new_id1)
    return new_id1

print(solution("abcdefghijklmn.p"))