def solution(board):
    answer = 0
    bomb_place = [[-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [1, -1], [1, 1]]
    bomb_list = []
    
    if len(board[0]) * len(board) == sum([sum(i) for i in board]):
        return 0
    
    for i, v in enumerate(board):
        for j, v2 in enumerate(v):
            if v2 == 1:
                bomb_list.append([i, j, v2])
                
    for bomb in bomb_list:
        x = bomb[0]
        y = bomb[1]
        for place in bomb_place:
            dx = x + place[0]
            dy = y + place[1]
            
            if dx < 0 or dx >= len(board[0]) or dy < 0 or dy >= len(board):
                continue
            
            board[dx][dy] = 1
            
    return sum([1 for i in board for j in i if j == 0])