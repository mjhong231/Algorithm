
n = int(input())
stack = []
now = 1
ans = []
for tc in range(n):
    num = int(input())
    
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        print('NO')
        break

else:
    for a in ans:
        print(a)
