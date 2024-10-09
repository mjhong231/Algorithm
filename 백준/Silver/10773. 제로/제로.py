import sys
input = sys.stdin.readline
K = int(input())
stack = []
for _ in range(1, K+1):
    i = int(input())
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))