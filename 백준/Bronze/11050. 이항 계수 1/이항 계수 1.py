import sys
input = sys.stdin.readline


N, K = map(int, input().split())

def fac(level):
    if level == 0 or level == 1:
        return 1
    else:
        return level * fac(level-1)

print(fac(N) // (fac(K) * fac(N - K)))
