
sugar = int(input())

gram = 0

while sugar >= 0:
    if sugar % 5 == 0:
        gram += (sugar // 5)
        print(gram)
        break
    sugar -= 3
    gram += 1
else: print(-1)




