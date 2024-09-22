import sys
from collections import Counter
input = sys.stdin.readline


N = int(input())
nums = [int(input()) for _ in range(N)]
# 산술평균
print(round(sum(nums)/N))

#중앙값
nums.sort()
print(nums[N//2])

#최빈값
cnt = Counter(nums)
most = cnt.most_common()

if len(most) == 1 or most[0][1] != most[1][1]:
    print(most[0][0])
else:
    print(most[1][0])

#차이
print(max(nums) - min(nums))