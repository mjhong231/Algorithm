import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 앱의 개수 N, 확보해야 하는 메모리 M
apps = [0] + list(map(int, input().split()))  # 앱이 사용하는 메모리
costs = [0] + list(map(int, input().split()))  # 앱 비활성화 비용

if M == 0:  # 확보해야 할 메모리가 0인 경우
    print(0)
    sys.exit()

max_cost = sum(costs)  # 비용의 총합 계산
dp = [0] * (max_cost + 1)  # 1차원 DP 배열로 변경

result = max_cost  # 최소 비용 초기화

for i in range(1, N + 1):
    byte = apps[i]
    cost = costs[i]

    # 비용을 높은 값부터 낮은 값으로 탐색 (역순으로 탐색해야 이전 상태를 덮어쓰지 않음)
    for j in range(max_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + byte)

# 최소 비용 탐색
for j in range(max_cost + 1):
    if dp[j] >= M:
        result = j
        break

print(result)