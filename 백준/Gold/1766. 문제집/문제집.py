import sys, heapq
inpyt = sys.stdin.readline

N, M = map(int, input().split())  # 문제수 N / 먼저 푸는 것이 좋은 수 M
problems = [[] for _ in range(N+1)]
indegrees = [0] * (N+1) # 문제는 1번부터 시작

for _ in range(M):
    A, B = map(int, input().split())
    problems[A].append(B)
    indegrees[B] += 1

hq = []
result = []

for problem in range(1, N+1):
    if indegrees[problem] == 0:
        heapq.heappush(hq, problem)

while hq:
    now = heapq.heappop(hq)
    result.append(now)

    for next_problem in problems[now]:
        indegrees[next_problem] -= 1
        if indegrees[next_problem] == 0:
            heapq.heappush(hq, next_problem)

print(*result)