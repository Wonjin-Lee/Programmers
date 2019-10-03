def solution(board):

    #table = [[1 if x == "O" else 0 for x in sub_board] for sub_board in board]

    answer = 0

    if 1 in board[0]:
        answer = 1

    for x in range(1, len(board)):
        for y in range(1, len(board[x])):
            if board[x][y] == 0:
                continue

            board[x][y] = min(board[x][y-1], board[x-1][y], board[x-1][y-1]) + 1
            if board[x][y] > answer:
                answer = board[x][y]
    
    return pow(answer, 2)

print(solution([[1,0],[0,0]]))