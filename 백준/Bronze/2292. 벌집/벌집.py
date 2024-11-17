num = int(input())
lst = 1
cnt = 1

while num > lst:
    lst += 6 * cnt
    cnt += 1
print(cnt)