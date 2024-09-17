
N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
N_lst.sort()

for m in M_lst:
    left, right = 0, N - 1

    while left <= right:
        mid = (left+right) // 2
        if m > N_lst[mid]:
            left = mid + 1
        elif m < N_lst[mid]:
            right = mid - 1
        else:
            left, right = mid, mid
            break
    if left == mid and right == mid:
        print(1)
    else:
        print(0)