import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))


for i in range(1,N+1):
    if i > 0:
        nums[i] = nums[i-1] + nums[i]

for tc in range(1, M+1):
    i, j = map(int, input().split())

    print(nums[j] - nums[i-1])
