def bingo(board):  
    bingo_count = 0  
    
    for row in board:
        if row.count(0) == 5:
            bingo_count += 1

    for i in range(5):
        cnt1 = 0
        for j in range(5):
            if board[j][i] == 0:
                cnt1 += 1
        if cnt1 == 5:
            bingo_count += 1


    cnt2 = 0
    for i in range(5):
        if board[i][i] == 0:
            cnt2 += 1
    if cnt2 == 5:
        bingo_count += 1


    cnt3 = 0
    for i in range(5):
        if board[i][4 - i] == 0:
            cnt3 += 1
    if cnt3 == 5:
        bingo_count += 1

    return bingo_count


def find_bingo(board, mc):  
    for i in range(25):
        for j in range(5):
            for k in range(5):
                if board[j][k] == mc[i]:  
                    board[j][k] = 0  

        if bingo(board) >= 3:  
            return i + 1 

board = [list(map(int, input().split())) for _ in range(5)]  

mc = [int(i) for _ in range(5) for i in input().split()]  

result = find_bingo(board, mc)
print(result)
