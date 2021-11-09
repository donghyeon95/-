def sol(input_str, String, where):
    new_str = ""
    last = 0
    
    for index in where:
        if index == 0:
            new_str += input_str
            last = index
        else:
            new_str += String[last+1: index] + input_str
            last = index
    if last < len(String)-1:
        new_str += String[last+1 : ]

    return new_str


if __name__ == "__main__":
    input_str= input()
    String = input()
    N = int(input())
    min_num, max_num = list(map(int, input().split()))
    
    where = []
    for index in range(len(String)):
        if String[index] == '$':
            where.append(index)
    
    for i in range(N):
        input_str = sol(input_str, String, where)
    print(input_str[min_num-1: max_num])