def program(level):
    global num
    if level > N:
        return num 

    num *= level
    return program(level + 1) 


N = int(input())  
num = 1
result = program(1)  
lst = list(str(result))  
cnt = 0  

for i in range(len(lst) - 1, -1, -1):
    if lst[i] == '0':  
        cnt += 1
    else:
        break  

print(cnt) 
