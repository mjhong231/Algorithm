T = int(input())

for tc in range(1, T+1):
    stack = []
    S = input()

    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')