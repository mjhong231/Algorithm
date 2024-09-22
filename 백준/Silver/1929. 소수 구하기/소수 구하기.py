import sys

def program(num):

    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

N, M = map(int, sys.stdin.readline().split())
for j in range(N, M+1):
    if program(j):
        print(j)

