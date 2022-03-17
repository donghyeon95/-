'''
프로그래머스 2022 카카오 리쿠르먼트
'''

import math
import re 
def getNum(n, k):
    num = ""   
    while True:
        if n <= k:
            num = str(n) + num
            break
        remain = n%k
        n = n // k
        num = str(remain) + num
    return num
        
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    
    answer = 0
    num = getNum(n, k)
    li = re.split(r'0+', num)
    
    for i in li :
        if i != "" and i != "1" and is_prime(int(i)):
            answer += 1

    return answer