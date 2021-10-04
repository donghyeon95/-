def solution(rows, columns, queries):
    answer = []
    
    # 2차원 배열 선언
    table = [[0 for col in range(columns)] for row in range(rows)]

    # 배열에 값 추가
    v = 1
    for row in range(rows):
        for col in range(columns):
                table[row][col] = v
                v+=1

    # queries의 갯수만큼 반복
    for i in range(len(queries)):
        # 회전할 모서리 값 저장
        c1 = queries[i][0] - 1
        r1 = queries[i][1] - 1
        c2 = queries[i][2] - 1
        r2 = queries[i][3] - 1
        
        # 값을 회전하다보면 하나의 값이 덮어씌워지기때문에 미리 저장
        temp = table[c1][r1]

        small = float('inf')


        # r1열 값 회전 (r1값 고정)
        for c in range(c1, c2):
            table[c][r1] = table[c+1][r1]
            #최소값 비교
            if table[c][r1] < small:
                small = table[c][r1]

        # c2행 값 회전 (c2값 고정)
        for r in range(r1, r2):
            table[c2][r] = table[c2][r+1]
            # 최소값 비교
            if table[c2][r] < small:
                small = table[c2][r]

        # r2열 값 회전 (r2값 고정)
        for c in range(c2, c1, -1):
            table[c][r2] = table[c-1][r2]
            # 최소값 비교
            if table[c][r2] < small:
                small = table[c][r2]

        # c1행 값 회전 (c1값 고정)
        for r in range(r2, r1, -1):
            table[c1][r] = table[c1][r-1]

            # 최소값 비교
            if table[c1][r] < small:
                small = table[c1][r]

        #table[c1][r1+1]에 임시로 저장해놨던 temp값 붙여넣기
        table[c1][r1+1] = temp

        #temp와 최소값 비교
        if table[c1][r1+1] < small:
            small = table[c1][r1+1]

        answer.append(small)

    return answer