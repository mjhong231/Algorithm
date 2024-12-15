import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

P = 'IO'*N + 'I'

cnt = 0
for i in range(M):
  if S[i] == 'I':
    if S[i:i+(N*2+1)] == P and i <= M:
      cnt += 1

print(cnt)