
import sys

M = int(sys.stdin.readline())

S = set()

for tc in range(M):
    temp = sys.stdin.readline().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()
    else:
        order, num = temp[0], int(temp[1])
        if order == 'add':
            S.add(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'remove':
            if num in S:
                S.discard(num)
        elif order == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
