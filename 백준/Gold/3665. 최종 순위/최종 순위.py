from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    team = list(map(int, input().rstrip().split()))
    
    lst = {i: [] for i in range(1, n+1)}
    indegree = {i: 0 for i in range(1, n+1)}

    # 초기 순위 그래프 구성
    for i in range(n-1):
        for j in range(i+1, n):
            lst[team[i]].append(team[j])
            indegree[team[j]] += 1

    # 순위 변경 요청 처리
    m = int(input())
    for _ in range(m):
        fir, sec = map(int, input().rstrip().split())

        if sec in lst[fir]:
            lst[fir].remove(sec)
            indegree[sec] -= 1
            lst[sec].append(fir)
            indegree[fir] += 1
        else:
            lst[sec].remove(fir)
            indegree[fir] -= 1
            lst[fir].append(sec)
            indegree[sec] += 1

    # 위상 정렬 수행
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    if not q:
        print("IMPOSSIBLE")
        continue

    ans = []
    is_certain = True

    while q:
        if len(q) > 1:
            is_certain = False
            break

        current = q.popleft()
        ans.append(current)

        for neighbor in lst[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if not is_certain or len(ans) != n:
        print("IMPOSSIBLE")
    else:
        print(*ans)
