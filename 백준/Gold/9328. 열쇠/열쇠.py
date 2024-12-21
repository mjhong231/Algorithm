
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
results = []

for tc in range(T):
    h, w = map(int, input().split())

    # 지도 초기화
    lst = []
    lst.append(["." for _ in range(w + 2)])
    for _ in range(h):
        lst.append(list("." + input().strip() + "."))
    lst.append(["." for _ in range(w + 2)])

    # 열쇠 정보 초기화
    keys = [0 for _ in range(26)]
    for k in list(input().strip()):
        if k != "0":
            keys[ord(k) - 97] = 1

    # BFS 초기화
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    q = deque([(0, 0)])
    lst[0][0] = "*"  # 시작점 방문 처리

    papers = 0
    temp = [[] for _ in range(26)]  # 문을 임시 저장하는 배열

    # BFS 탐색
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and lst[ny][nx] != "*":
                num = ord(lst[ny][nx])
                if 65 <= num <= 90:  # 문
                    if keys[num - 65] == 0:
                        temp[num - 65].append((ny, nx))  # 열쇠가 없으면 저장
                        continue
                elif 97 <= num <= 122:  # 열쇠
                    if keys[num - 97] == 0:  # 새로운 열쇠
                        keys[num - 97] = 1
                        for t in temp[num - 97]:  # 열쇠로 문 열기
                            q.append(t)
                elif lst[ny][nx] == "$":  # 서류 발견
                    papers += 1

                lst[ny][nx] = "*"  # 방문 처리
                q.append((ny, nx))

    results.append(papers)

# 결과 출력
for r in results:
    print(r)
