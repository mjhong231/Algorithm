from collections import deque

A, B = map(int, input().split())

def bfs():
    q = deque([(A, 1)])  # (스타트숫자, cnt)

    while q:
        now, cnt = q.popleft()

        if now == B:
            return cnt

        # 노드 2개 
        firstnode = now * 2
        secondnode = int(str(now) + '1')

        if firstnode <= B:  
            q.append((firstnode, cnt + 1))
        if secondnode <= B:  
            q.append((secondnode, cnt + 1))

    return -1  


print(bfs())