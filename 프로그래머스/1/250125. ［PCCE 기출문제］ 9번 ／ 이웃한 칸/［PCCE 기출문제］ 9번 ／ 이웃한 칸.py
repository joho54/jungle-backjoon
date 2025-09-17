def solution(board, h, w):
    answer = 0
    n = len(board)
    for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
        nx, ny = h + dx, w + dy
        if 0 <= nx < n and 0 <= ny < n:
            answer += 1 if board[nx][ny] == board[h][w] else 0
    return answer