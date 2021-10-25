a, b = input().split()



a = list(a)
b = list(b)

a.reverse()
b.reverse()


a = "".join(a)
b = "".join(b)



print(int(a)+int(b))