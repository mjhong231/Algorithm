
N = int(input())
lst = []
for tc in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(key=lambda x: (x[0], x[1]))

for l in lst:
    print(*l)