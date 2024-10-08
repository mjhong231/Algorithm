N = int(input())
arr = list(map(int, input().split()))
lst = []
for num, idx in enumerate(arr):
    lst.append([num, idx])
lst.sort(key=lambda x: x[1])
cnt = -1
temp = float("inf")

for i in range(N):
    if temp != lst[i][1]:
        cnt += 1
        temp = lst[i][1]
    lst[i][1] = cnt

lst.sort()

for l, s in lst:
    print(s, end = ' ')
print()
