import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    closet = dict()

    for _ in range(1, N+1):
        cloth, category = input().split()
        if category in closet:
            closet[category].append(cloth)
        else:
            closet[category] = [cloth]

    cnt = 1

    for c in closet.values():
        cnt *= len(c) + 1

    print(cnt - 1)
