
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []


def program(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N):

        
        path.append(arr[i])
        program(i, level+1)
        path.pop()
       
program(0, 0)

