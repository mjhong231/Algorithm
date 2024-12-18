import sys
input = sys.stdin.readline

V, E = map(int, input().split())

lst = []

for _ in range(E):
    A, B, C = map(int, input().split())
    lst.append((A, B, C))
lst.sort(key=lambda x:x[2])

parents = [i for i in range(V+1)]

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

result = 0

for a, b, cost in lst:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)