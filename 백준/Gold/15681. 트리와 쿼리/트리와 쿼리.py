import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_tree(cur_node, par_node):
    for node in graph[cur_node]:
        if node != par_node:
            children[cur_node].append(node)
            parent[node] = cur_node
            make_tree(node, cur_node)

def sub_tree(cur_node):
    for node in children[cur_node]:
        sub_tree(node)
        cnt_sub[cur_node] += cnt_sub[node]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
parent[R] = -1
children = [[] for _ in range(N+1)]
cnt_sub = [1] * (N+1)
make_tree(R, -1)
sub_tree(R)

for _ in range(Q):
    res = int(input())
    print(cnt_sub[res])