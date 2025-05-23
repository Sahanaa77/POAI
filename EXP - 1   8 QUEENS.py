N = 8

def printSolution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def isSafe(board, row, col):
    for i in range(row):
        if board[i][col] or (col - row + i >= 0 and board[i][col - row + i]) or (col + row - i < N and board[i][col + row - i]):
            return False
    return True

def solve(board, row):
    if row == N:
        print("One possible solution is:")
        printSolution(board)
        return True
    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0
    return False

def eightQueens():
    board = [[0] * N for _ in range(N)]
    if not solve(board, 0):
        print("Solution does not exist")

eightQueens()
