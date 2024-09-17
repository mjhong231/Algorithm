
N = int(input())
members = []
for tc in range(N):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for member in members:
    print(*member)

