import sys
from collections import deque

def sove1():
    n = int(input())
    a = [int(ai) for ai in input().split()]
    sum1 = sum(a[::2])
    sum2 = sum(a[1::2])
    return max(sum1,sum2)


def solu1():
    input = sys.stdin.readline
    T = int(input())
    for t in range(T):
        ans =  sove1()
        print(ans)

def solu2():
    input = sys.stdin.readline
    n, q = [int(x) for x in input().split()]

    adj = [[] * (n+1)]
    for _ in range(n-1):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)

    parent  = [0] * (n+1)
    parent[-1] = -1
    dq = deque([1])
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            dq.append(v)



    dis = [[] * (n+1)]
    q = deque([1])
    while q:
        now = q.popleft()
        sons = adj[now]
        if len(sons) == 1:
            pass

    # 由于需要多次询问，应该直接构建出来会比较好
    for _ in range(q):
        pass


def solu3():
    n = int(input())
    a = [int(ai) for ai in input().split()]
    a = sorted(a)
    s=0
    for n, ai in enumerate(a):
        for i in range(n):
            s += ai//a[i]
        s += 1
    print(s)



############################################################################
if __name__ == "__main__":
    solu3()
