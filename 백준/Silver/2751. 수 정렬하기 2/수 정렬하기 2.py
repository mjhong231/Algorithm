import sys

N = int(input())
lst = []
for _ in range(1, N+1):
    lst.append(int(sys.stdin.readline()))

for l in sorted(lst):
    print(l)