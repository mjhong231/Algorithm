N, M = map(int, input().split())
see = set()
listen = set()
result = []
for _ in range(N):
    see.add(input())

for _ in range(M):
    listen.add(input())

for i in see:
    if i in listen:
        result.append(i)

result.sort()
print(len(result))
for r in result:
    print(r)