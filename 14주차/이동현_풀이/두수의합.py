if __name__ == "__main__":
    with open(".input\input.txt", "r") as f:

        num_list = list(map(int, f.readline().split()))
        target = int(f.readline())

    for index in range(len(num_list)-1):
        for next in range(index+1, len(num_list)):
            if num_list[index]+num_list[next] == target :
                print(index, next)
                break

