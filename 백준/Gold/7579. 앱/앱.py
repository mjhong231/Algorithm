import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 앱의 개수 N, 확보해야하는 메모리 M
apps = [0] + list(map(int, input().split())) # 앱이 사용하는 메모리
costs = [0] + list(map(int, input().split())) # 앱 비활성화 비용

max_cost = sum(costs) # 비활성화 비용 총합
dp = [0] * (max_cost + 1) # 바텀업 방식

result = max_cost  # 최소 비용 초기화

for i in range(1, N+1):
    byte = apps[i]
    cost = costs[i]

    # 비용을 높은 값부터 낮은 값으로 탐색
    for j in range(max_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j-cost] + byte) 
        #dp[j]: 비활성화 비용(j)으로 확보할 수 있는 최대 메모리

for j in range(max_cost+1):
    if dp[j] >= M:
        result = j
        break
print(result)