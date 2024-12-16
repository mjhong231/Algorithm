import sys
input = sys.stdin.readline

N = int(input())   # IOI 패턴의 반복 횟수
M = int(input())   # 문자열 S의 길이
S = input().strip()  # 입력 문자열

now = 0  
cnt = 0
result = 0  

while now < M - 1:  
    if S[now:now + 3] == 'IOI':
        cnt += 1
        now += 2
        if cnt == N:
            result += 1
            cnt -= 1
    
    else:
        cnt = 0
        now += 1
        
print(result)