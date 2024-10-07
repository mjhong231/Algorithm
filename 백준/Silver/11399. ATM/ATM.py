
N = int(input())
times = sorted(list(map(int, input().split())))

sum_t = []
num = 0
for i in range(N):
    num += times[i]
    sum_t.append(num)
print(sum(sum_t))


