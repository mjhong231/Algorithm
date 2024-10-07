T = int(input())

for tc in range(1, T+1):
    N = int(input())

    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero + one
    print(zero, one)
