N = list(map(int, input().split()))
lst = [1, 1, 2, 2, 2, 8]
check = []

for i in range(6):
    num = lst[i] - N[i]
    check.append(num)

print(*check)
