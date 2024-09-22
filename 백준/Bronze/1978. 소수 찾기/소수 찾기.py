def program():
    cnt = 0
    for num in nums:
        prime = True  
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt


N = int(input())
nums = list(map(int, input().split()))
result = program()
print(result)


