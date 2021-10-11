# import re
# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
    
#     sp_char = "~!@#$%^&*()=+{[]}:?,<>/"
    
#     for char in sp_char:
#         new_id = new_id.replace(char, "")
#     new_id = re.sub('[.]{2,}',".",new_id)
    
#     if new_id[0] == '.':
#         new_id = new_id[1:]
#     if new_id == "":
#         return "aaa"
#     if new_id[-1] == ".":
#         new_id = new_id[:-1]
    
    
    
#     if len(new_id)>15:
#         new_id = new_id[:15]
#         if new_id[-1] ==".":
#             new_id = new_id[:-1]
    
#     if len(new_id)<3:
#         print(len(new_id), new_id[-1])
#         new_id = new_id + (new_id[-1]*(3-len(new_id)))

#     answer = new_id
    
    
    
#     return answer


# 정규식으로 해결...
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
