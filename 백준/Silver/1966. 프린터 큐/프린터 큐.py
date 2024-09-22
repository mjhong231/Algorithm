from collections import deque

T = int(input())
for tc in range(1, T+1):
    paper, target = map(int, input().split())
    order = list(map(int, input().split()))
    q = deque()
    for i in range(paper):
        q.append((order[i], i))

    num = 1 
    order.sort(reverse=True)  

    while q:
        qu = q.popleft()
        if qu[0] == order[num-1]: 
            if qu[1] == target:
                print(num)
                break
            num += 1
        else:
            q.append(qu)

