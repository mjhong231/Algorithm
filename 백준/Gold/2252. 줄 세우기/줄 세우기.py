
from collections import deque

import sys
input = sys.stdin.readline


N, M = map(int, input().split())  # M : 키를 비교한 횟수
heights = [[] for _ in range(N+1)]
indegrees = [0] * (N+1)  # 학생 번호는 1부터 시작

for _ in range(M):
    a, b =  map(int, input().split())  # a가 b 앞에 서야만 함 -> 위상정렬
    heights[a].append(b)
    indegrees[b] += 1

q = deque()  # 위상 정렬을 위한 큐 초기화
result = []

for height in range(1, N+1):
    if indegrees[height] == 0:
        q.append(height)

while q:
    now = q.popleft()
    result.append(now)  # 순서대로 학생 번호 추가

    for next_height in heights[now]:
        indegrees[next_height] -= 1
        if indegrees[next_height] == 0:
            q.append(next_height)

print(*result)


