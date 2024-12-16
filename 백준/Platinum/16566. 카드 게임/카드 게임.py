import sys, bisect
input = sys.stdin.readline

def find(a):
    while a != parents[a]:
        a = parents[a]
    return a
def union(a, b):
    if b >= M:
        return
    a = find(a)
    b = find(b)
    parents[a] = b

N, M, K = map(int, input().split()) # N개의 카드에서 M개를 뽑음
cards = list(map(int, input().split()))
choelsu = list(map(int, input().split()))
parents = [i for i in range(M)]
cards.sort()

for c in choelsu:
    idx = bisect.bisect_right(cards, c)
    idx = find(idx)
    print(cards[idx])
    union(idx, idx+1)