'''
문제 : 트리 그리기 과제
카테고리 : #tree
'''

if __name__ == '__main__':
    n, m = map(int, input().split())

    for i in range(n-m):
        print(i, i+1)
    for i in range(n-m, n-1):
        print(0, i+1)
