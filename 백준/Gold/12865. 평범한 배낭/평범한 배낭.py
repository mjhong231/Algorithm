import sys
input = sys.stdin.readline

# 물품의 수 N / 버틸 수 있는 무게 K
N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(1, N+1):
    stuff.append((list(map(int, input().split())))) # 물건의 (무게, 가치)

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j - weight], knapsack[i-1][j])

print(knapsack[N][K])
