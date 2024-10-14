import sys, math
input = sys.stdin.readline

A, B, V = map(int, input().split())

cnt = (V-B) / (A -B)

print(math.ceil(cnt))