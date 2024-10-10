
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []

def program(x, y, N):
    color = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                program(x, y, N//2)
                program(x, y+N//2, N//2)
                program(x+N//2, y, N//2)
                program(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

program(0, 0, N)
print(result.count(0))
print(result.count(1))
