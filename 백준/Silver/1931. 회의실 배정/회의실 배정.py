N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
last_time = meetings[0][1]

for i in range(1, N):
    if meetings[i][0] >= last_time:
        cnt += 1
        last_time = meetings[i][1]

print(cnt)