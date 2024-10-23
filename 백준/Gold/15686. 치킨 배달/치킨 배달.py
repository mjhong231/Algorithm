from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
houses = []  # 집
chickens = [] # 치킨집

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] == 1:
            houses.append((i, j))

for chicken in combinations(chickens, M):
    temp = 0  # 치킨거리 초기화
    for house in houses:
        chicken_len = float('inf')
        for j in range(M):
            chicken_len = min(chicken_len, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))
        temp += chicken_len
    result = min(result, temp)


print(result)
