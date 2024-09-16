N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []

def program(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path.append(arr[i])
        program(level+1)
        path.pop()


program(0)