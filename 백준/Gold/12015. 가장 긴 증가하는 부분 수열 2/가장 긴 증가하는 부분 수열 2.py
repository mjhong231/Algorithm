import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

lst = [0]

for a in arr:
    if lst[-1] < a:
        lst.append(a)
    else:
        left = 0
        right = len(lst)

        while left < right:
            mid = (left + right) // 2
            if lst[mid] < a:
                left = mid + 1

            else:
                right = mid
        lst[right] = a

print(len(lst) - 1)