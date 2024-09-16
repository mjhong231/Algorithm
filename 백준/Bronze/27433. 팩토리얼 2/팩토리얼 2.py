
N = int(input())
path = 1

def program(level):
    global path
    if level > N:
        print(path)
        return

    path *= level
    program(level + 1)

program(1)
