import sys

def solu1():
    n = input()
    s = sum([int(x)**3 for x in n])

    if int(n) == s:
        print("YES") 
        return
    print("NO")


def solu2():
    pass



############################################################################
if __name__ == "__main__":
    solu1()