s=input()
S=input()
cnt = int(input())
start,end = map(int,input().split())

def solve(cnt,s,S,end):
    if len(s) >= end:
        return s
    text = ""
    if cnt == 0:
        return s
    for t in S:
        if t == "$":
            text += s
        else:
            text += t
    return solve(cnt-1,text,S,end)

print(solve(cnt,s,S,end)[start-1:end])
     









str1 = input()
str_list = input().split('$')
str_list = str_list[1:-1]
re_time = int(input())
min_str,max_str = map(int,input().split())
data = str1
i = 0
while len(data) < max_str:
    if len(str_list) == 0:
        data += str1
    else:
        data += str_list[i%len(str_list)] + str1
    i += 1
# def fes(data):
#     if i > re_time:
#         return '-'
#     if len(data) >= max_str:
#         return data[min_str-1:max_str]
#     data += str_list[i%len(str_list)] + str1
#     return data + fes(data)
if i >= re_time :
    print('-')
else:
    print(data[min_str-1:max_str])















