import sys
input = sys.stdin.readline

n = int(input())

lst = {}  # 딕셔너리

for _ in range(n):
    node, left, right = map(str, input().split())
    lst[node] = [left, right]


def pre(root):
    if root != '.':
        print(root, end = '')
        pre(lst[root][0])
        pre(lst[root][1])

def inorder(root):
    if root != '.':
        inorder(lst[root][0])
        print(root, end = '')
        inorder(lst[root][1])


def post(root):
    if root != '.':
        post(lst[root][0])
        post(lst[root][1])
        print(root, end = '')

pre('A')
print()
inorder('A')
print()
post('A')
