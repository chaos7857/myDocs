def solu1():
    N = int(input())
    if not N&1: return
    n = [int(ni) for ni in input().split()]


def solu2(n,m,h,data):

    adj = [[] * (n+1)]
    for i in data:
        if h[i[0]] > h[i[1]]:
            adj[i[0]].append(i[1])
        else:
            adj[i[1]].append(i[0])


    order = list(range(n))
    order.sort(key=lambda x: (h[x], x))

    dp = [1] * n

    for i in order:
        for v in adj[i]:
            dp[i] = max(dp[i], dp[v] + 1)

    print(max(dp))




if __name__ == "__main__":
    '''your description here'''
    # -------------------------------------------
    solu1()
    # -------------------------------------------
    print("done.")