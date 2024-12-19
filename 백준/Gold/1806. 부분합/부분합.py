N, S = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
sum_V = 0
min_len = float('inf')

while True:
    if sum_V >= S:
        min_len = min(min_len, right - left)
        sum_V -= lst[left]
        left += 1
    elif right == N:
        break
    else:
        sum_V += lst[right]
        right += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)
