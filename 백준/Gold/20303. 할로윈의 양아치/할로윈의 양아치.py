import sys
input = sys.stdin.readline

def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))
parents = [i for i in range(N+1)]
friends = [1] * (N+1)  # 자기 자신

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N+1):
    root = find(i)
    if i != root:
        candies[root] += candies[i]
        friends[root] += friends[i]

# DP 배열 초기화
dp = [0] * K

# DP 갱신
for i in range(1, N+1):
    if i == find(i):  # 루트 노드만 처리
        for j in range(K-1, friends[i]-1, -1):
            dp[j] = max(dp[j], dp[j-friends[i]] + candies[i])

# 최대 사탕 출력
print(max(dp))