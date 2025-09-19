import sys
from collections import deque
def solu1():
    lines_words = []
    max_cols = 0
    for line in sys.stdin.readlines():
        words = line.strip().split()
        if words:
            lines_words.append(words)
            if len(words) > max_cols:
                max_cols = len(words)
    if not lines_words: return
    #######################################
    max_lengths  = [0] * max_cols
    for words in lines_words:
        for i, word in enumerate(words):
            if len(word) > max_lengths[i]:
                max_lengths[i] = len(word)

    #######################################
    positions = [0] * max_cols
    if max_cols > 0:
        positions[0] = 1# p_1 = 1
    if max_cols > 1:
        # p_2 = M_1 + 2
        positions[1] = max_lengths[0] + 2
    for k in range(2, max_cols):
        # p_{k+1} = p_k + M_k + 1
        positions[k] = positions[k-1] + max_lengths[k-1] + 1

    # 4. 格式化并输出结果
    for words in lines_words:
        output_line = []
        # 添加第一个词
        if len(words) > 0:
            output_line.append(words[0])
        
        # 添加后续的词和所需空格
        for j in range(1, len(words)):
            # 计算上一个词的结束位置后的光标位置
            # p_j + L_{i,j}
            current_pos = positions[j-1] + len(words[j-1])
            # 计算需要填充的空格数
            spaces_to_add = positions[j] - current_pos
            
            # 添加空格和单词
            output_line.append(' ' * spaces_to_add)
            output_line.append(words[j])
        
        print("".join(output_line))

def bfs(start_node, n, adj):
    """
    执行广度优先搜索来找到从start_node出发的最远节点及其距离。
    :param start_node: 起始节点
    :param n: 节点总数
    :param adj: 邻接表
    :return: 一个元组 (最远节点, 最大距离)
    """
    # dist数组用于存储距离，-1表示未访问
    dist = [-1] * (n + 1)
    # 使用deque作为高效队列
    queue = deque()

    # 初始化起始节点
    dist[start_node] = 0
    queue.append(start_node)

    while queue:
        u = queue.popleft()
        
        # 遍历当前节点的所有邻居
        for v, weight in adj[u]:
            # 如果邻居未被访问
            if dist[v] == -1:
                dist[v] = dist[u] + weight
                queue.append(v)
    
    # 遍历所有节点的距离，找到最远的一个
    max_dist = -1
    farthest_node = -1
    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest_node = i
            
    return farthest_node, max_dist

def bfs_rewrite(start, n, adj):
    dist = [-1] * (n+1)
    que = deque()

    dist[start] = 0
    que.append(start)

    while que:
        now = que.popleft()
        for node, weight in adj[now]:
            if dist[node] == -1:
                dist[node] = weight + dist[now]
                que.append(node)

    # 构建完距离表，现在从表中找到最远距离和节点
    far_node = -1
    far_dist = -1
    for a, dist_ in enumerate(dist):
        if dist_>far_dist:
            far_dist = dist_
            far_node = a
    
    return far_node, far_dist

def solu2():
    input = sys.stdin.readline
    try:
        n_str = input()
        if not n_str: return
        n = int(n_str)
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v, w = map(int, input().split())
            adj[u].append((v, w))
            adj[v].append((u, w))

        endpoint, _ = bfs(1, n, adj)
        _, diameter = bfs(endpoint, n, adj)
        max_cost = diameter * (diameter + 21) // 2
        print(max_cost)
    except (IOError, ValueError, IndexError):
        return
######################################################################
def bfs3(start, n, adj):
    dist = [-1] * (n+1)
    que = deque()

    dist[start] = 0
    que.append(start)
    
    while que:
        now = que.popleft()
        for node, weight in adj[now]:
            if dist[node] == -1:
                dist[node] = weight + dist[now]
                que.append(node)
    
    # 最短路径
    path_len = dist[1]
    print(path_len)

    # 第二步：逐层构建理想路径
    current_nodes = {1}
    result_colors = []

    for _ in range(path_len):
        min_color = float('inf')
        
        # 找到当前层所有可达边中的最小颜色
        for u in current_nodes:
            for v, c in adj[u]:
                # 必须是走向终点的最短路径
                if dist[v] == dist[u] - 1:
                    min_color = min(min_color, c)
        
        result_colors.append(min_color)
        
        # 找到所有通过最小颜色边可达的下一层节点
        next_nodes = set()
        for u in current_nodes:
            for v, c in adj[u]:
                if dist[v] == dist[u] - 1 and c == min_color:
                    next_nodes.add(v)
        
        current_nodes = next_nodes

        print(*result_colors)


def solu3():
    input = sys.stdin.readline
    N, M = [int(x) for x in input().split()]
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        ai, bi, ci = [int(x) for x in input().split()]
        adj[ai].append([bi, ci])
        adj[bi].append([ai, ci])
    
    bfs3(N, N, adj)

    
############################################################################
if __name__ == "__main__":
    solu3()