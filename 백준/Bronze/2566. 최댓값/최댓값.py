def find(arr):
    max_v = float('-inf')  
    max_x, max_y = 0, 0    #

    for i in range(9):
        for j in range(9):
            if arr[i][j] > max_v:
                max_v = arr[i][j] 
                max_x, max_y = i, j 

    return max_v, max_x, max_y

arr = [list(map(int, input().split())) for _ in range(9)]
result, max_x, max_y = find(arr)

print(result)
print(max_x+1, max_y+1)  
