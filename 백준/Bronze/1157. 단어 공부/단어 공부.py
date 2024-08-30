S = input().upper()
S_lst = list(set(S))

cnt = []
for i in S_lst:
    cnt.append(S.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(S_lst[cnt.index(max(cnt))])

