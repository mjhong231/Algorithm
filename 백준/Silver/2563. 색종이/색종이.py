def check(x, y, arr): 
    for i in range(x, x+10):
        idx_x = i
        for j in range(y, y+10):
            idx_y = j
            if arr[idx_x][idx_y] == 0:
                arr[idx_x][idx_y] = 1

def total(arr):
    total = 0
    for k in range(100):
        total += sum(arr[k])
    return total

N = int(input())
arr = [[0] * 100 for _ in range(100)]
for tc in range(N):
    x, y = map(int, input().split())
    check(x, y, arr)  

result = total(arr) 
print(result)