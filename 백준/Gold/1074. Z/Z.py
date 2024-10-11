
N, r, c = map(int, input().split()) 

def program(N, r, c):
    if N == 0:
        return 0

    return 2*(r%2) + (c%2) + 4*program(N-1, int(r/2), int(c/2))

print(program(N, r, c))