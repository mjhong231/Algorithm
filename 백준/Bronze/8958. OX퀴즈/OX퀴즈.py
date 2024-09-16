def program():
    cnt = 0
    score = 0
    for i in range(len(Q)):
        if Q[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    return score

T = int(input())
for tc in range(1, T+1):
    Q = list(input())

    result = program()
    print(result)