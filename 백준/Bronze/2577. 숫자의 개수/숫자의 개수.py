
def program():

    lst = [0] * 10
    lst_num = list(str(num))
    for i in lst_num:
        lst[int(i)] += 1

    return lst


A = int(input())
B = int(input())
C = int(input())
num = A * B * C
result = program()
for r in result:
    print(r)