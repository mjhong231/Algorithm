import sys
input = sys.stdin.readline

def find(a):
    while a != parents[a]:
        a = parents[a]
    return a

def union(a, b):
    a = find(a)
    b= find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
lst = []
parents = [i for i in range(N+1)]
for _ in range(M):
    A, B, cost = map(int, input().split())
    lst.append((A, B, cost))
lst.sort(key=lambda x:x[2])  # cost순으로 정렬

result = 0
big = 0

for a, b, c in lst:
    if find(a) != find(b):
        union(a, b)
        result += c
        big = c
print(result - big)