
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split()) # 노드의 개수 N / 연산의 개수 M
parents = [0] * (N+1) # 부모노드를 저장할 리스트

for i in range(1, N+1):
    parents[i] = i  # 초기세팅(각 노드가 자기 자신을 부모로 가지도록 설정)

def find(a):
    # 만약 a가 루트노드가 아니라면
    if parents[a] != a:
        parents[a] = find(parents[a]) # 경로압축해서 루트 노드 갱신
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    # 값이 작은 루트 노드를 상위 부모로 설정
    if a < b:
        parents[b] = a  # b의 부모를 a로 설정
    else:
        parents[a] = b


for _ in range(M):
    op, a, b = map(int, input().split())

    if op == 0: # 합치기(union)
        union(a, b)
    
    else:  # 같은 집합에 속해 있는지 확인(find)
        if find(a) == find(b):
            print('YES')  # 같은 집합에 속함
        else:
            print('NO')  # 다른 집합에 속함