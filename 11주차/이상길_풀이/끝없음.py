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
     
