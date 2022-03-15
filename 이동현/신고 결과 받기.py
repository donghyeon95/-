'''
프로그래머스 2022 카카오 리쿠르먼트
'''

import collections

def solution(id_list, report, k):
    
    users = collections.defaultdict(list)
    name = {}
    ans = [0] * len(id_list) 
    
    for idx, user in enumerate(id_list):
        users[user]
        name[user] = idx
        
    for repo in report:
        reporter, reportee = repo.split()
        if reporter not in users[reportee] :
            # ans[name[reporter]] +=1
            users[reportee].append(reporter)
    # print(users)
    repo_list = users.values()
    for idx, repo in enumerate(repo_list):
        if len(repo) >= k :
            for ur in repo:
                ans[name[ur]] += 1
        
    
    
    
    
    return ans