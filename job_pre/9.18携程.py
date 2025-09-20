import sys
input = sys.stdin.readline

def solu1():
    n = input()
    s = sum([int(x)**3 for x in n])

    if int(n) == s:
        print("YES") 
        return
    print("NO")

#################################################################
def solu2():

    n = int(input())
    s = input().strip()

    s = [ord(si) for si in s]
    # 从左向右替换
    for i, si in enumerate(s):
        # a 97     z 122
        # A 65     Z 90
        # print(ord(si))
        
        if si == 97:
            s[i] = 122
        elif si == 90:
            s[i] = 65
        elif si in range(98,123):
            s[i] -= 1
        elif si in range(65,90):
            s[i] += 1

    s = [chr(si) for si in s]
    # print(s)

    
    res = []
    # 从右向左删除
    cnt=0
    for si in reversed(s):
        
        if cnt & 1:
            if res and si == res[-1]:
                cnt+=1
                continue
            else:
                res.append(si)
                cnt=0

        else:
            if res and si.lower() == res[-1].lower() and si != res[-1]:
                cnt+=1
                continue
            else:
                res.append(si)
                cnt=0
    
            
    
    print(''.join(reversed(res)))

    



############################################################################
if __name__ == "__main__":
    solu2()