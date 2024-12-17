import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [] ,[]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

start, end = 0, N ** 2-1
cnt = 0

while start < len(AB) and end >= 0:
    if AB[start] + CD[end] == 0:
        cnt_start, cnt_end = start + 1, end - 1

        while cnt_start < len(AB) and AB[start] == AB[cnt_start]:
            cnt_start += 1

        while cnt_end >= 0 and CD[end] == CD[cnt_end]:
            cnt_end -= 1

        cnt += (cnt_start - start) * (end - cnt_end)
        start, end = cnt_start, cnt_end

    elif AB[start] + CD[end] > 0:
        end -= 1

    else:
        start += 1

print(cnt)