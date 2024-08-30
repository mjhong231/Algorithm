def paper(x1, y1, x2, y2, arr):

    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i][j] == 0:
                arr[i][j] = 1

def total(arr):
    total = 0
    for k in range(len(arr)):
        total += sum(arr[k])
    return total

arr = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    paper(x1, y1, x2, y2, arr)

result = total(arr)
print(result)