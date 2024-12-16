
import sys
input = sys.stdin.readline


def find(a):
    while a != parents[a]:
        a = parents[a]

    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

cnt = 0

N, M = map(int, input().split())
parents = [i for i in range(N)]

for i in range(1, M+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cnt = i
        break
    union(a, b)

print(cnt)