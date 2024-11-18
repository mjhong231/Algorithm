from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 건물 개수 N과 건물 간의 건설 순서 규칙 개수 K
    lst = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]  # 위상 정렬을 위한 indegree

    times = list(map(int, input().split()))  # 건물당 건설에 걸리는 시간
    for _ in range(K):
        x, y = map(int, input().split())  # 선행 순서 x -> y
        lst[x].append(y)
        indegree[y] += 1
    w = int(input())  

    q = deque()
    result = [0 for _ in range(N + 1)]  # 각 건물의 건설 완료 시간을 저장

    for node in range(1, N + 1):
        if indegree[node] == 0:
            q.append(node)
            result[node] = times[node - 1]

    while q:
        now = q.popleft()
        for next_node in lst[now]:
            indegree[next_node] -= 1
            result[next_node] = max(result[next_node], result[now] + times[next_node - 1])
            if indegree[next_node] == 0:
                q.append(next_node)

    print(result[w])
