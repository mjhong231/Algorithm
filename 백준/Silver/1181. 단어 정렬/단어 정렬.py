
N = int(input())
lst = []
for tc in range(1, N+1):
    word = input()
    lst.append(word)
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
for l in lst:
    print(l)