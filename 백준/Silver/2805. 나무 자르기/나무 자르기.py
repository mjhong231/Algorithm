import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N = 나무의 수, M = 집에 가져가야할 나무 수

trees = sorted(list(map(int, input().split())))

def bs():
    start = 1
    end = max(trees)
    result = 0

    while start <= end:
        mid = (start+end) // 2
        target = 0

        for tree in trees:
            if tree >= mid:
                target += tree - mid


        if target >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(bs())