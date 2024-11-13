import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

check = float('inf')
ans = [float('inf'), float('inf')]

left, right = 0, N-1  # 인덱스

while left < right:
    if abs(lst[left]+lst[right]) < check:
        check = abs(lst[left]+lst[right])
        ans = [lst[left], lst[right]]

    if lst[left]+lst[right] < 0:
        left += 1

    else:
        right -= 1

print(*ans)

