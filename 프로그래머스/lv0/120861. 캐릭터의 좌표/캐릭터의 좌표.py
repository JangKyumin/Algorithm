def solution(keyinput, board):
    x, y = 0, 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    move_types = ['left', 'right', 'up', 'down']
    
    for key in keyinput:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
                
            if key == move_types[i]:
                
                if (y + dy[i] > (board[1] // 2) or y + dy[i] < -(board[1] // 2)) or (x + dx[i] > (board[0] // 2) or x + dx[i] < -(board[0] // 2)):
                    break
                
                nx = x + dx[i]
                ny = y + dy[i]
                

        # 이동 수행
        x, y = nx, ny
    
    return [x, y]