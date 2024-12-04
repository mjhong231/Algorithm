import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

lst = [arr[0]]

dp = [(0, arr[0])]

def b(target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start+end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, N):
    if arr[i] > lst[-1]:
        lst.append(arr[i])
        dp.append((len(lst)-1, arr[i]))
    else:
        idx = b(arr[i])
        lst[idx] = arr[i]
        dp.append((idx, arr[i]))

print(len(lst))

temp = len(lst) - 1
result = []
for i in range(len(dp) - 1, -1, -1):
    if dp[i][0] == temp:
        result.append(dp[i][1])
        temp -= 1

print(*result[::-1])
