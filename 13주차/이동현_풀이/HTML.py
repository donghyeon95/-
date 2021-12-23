from os import terminal_size


def enter(flag:bool=False):
    print()

    if flag == False:
        print("-"*80)
        return
    


if __name__ == "__main__":
    
    buffer = []
    temp = []
    flag = False
    special = False
   
    # with open(".input/input.txt") as f:
    #     while True:
    #         line = f.readline() + " "
    #         for char in line:
    #             if char==" " and flag==True:
    #                 continue
    #             if char== " ":
    #                 flag=True
    #             else:
    #                 flag = False
                
    #             if char == "<":
    #                 special = True
    #                 continue
                
    #             if char == ">":
    #                 special = False
    #                 continue

    #             if special==True and char=="b":
    #                 enter()
    #                 buffer.clear()
    #                 continue

    #             elif special==True and char=="h":
    #                 enter(True)
    #                 buffer.clear()
    #                 continue

    #             elif special==True and char=="r":
    #                 continue
                    
    #             buffer.append(char)
    #             print(char, end="")
    #             if len(buffer)>80:
    #                 enter()
    #                 buffer.clear()
    while True:
        line = input()
        buffer.append(line)
        if line == "":
            break
    
    print(buffer)