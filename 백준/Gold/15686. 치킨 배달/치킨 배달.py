import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
houses = []  
chickens = [] 

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j)) 
        elif arr[i][j] == 1:
            houses.append((i, j))   

def dfs(start, path):
    global result
    if len(path) == M:  
        temp = 0  
        for house in houses: 
            chicken_len = float('inf')  
            for chicken in path: 
                chicken_len = min(chicken_len,  abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
            temp += chicken_len 
        result = min(result, temp)   
        return  

    for i in range(start, len(chickens)):  
        dfs(i+1, path + [chickens[i]])     

dfs(0, [])  

print(result)