N, M = map(int, input().split())
my_dict = {}
ans_lst = []
for tc in range(1, N+1):
    site, password = input().split()
    my_dict[site] = password

for i in range(M):
    qu = input()

    ans = my_dict[qu]
    ans_lst.append(ans)

for a in ans_lst:
    print(a)