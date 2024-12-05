import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
start, end = 1, max(lst)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for l in lst:
        cnt += l // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)