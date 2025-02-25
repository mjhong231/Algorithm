H, M = map(int, input().split())
time = int(input())

def cal():
    newH = H + (M+time) // 60
    newM = (M + time) % 60

    if newH >= 24:
        newH -= 24


    return newH, newM

result = cal()
print(*result)