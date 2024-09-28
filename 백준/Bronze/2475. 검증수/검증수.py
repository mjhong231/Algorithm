N = list(map(int, input().split()))
sum_v = 0
for i in N:
    sum_v += i * i

print(sum_v % 10)