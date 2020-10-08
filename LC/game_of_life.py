def gameOfLife(self, board: List[List[int]]) -> None:
    '''
    1. 1 w/ < 2 (1) neighbors dies
    2. 1 w/ > 3 live neighbors (1s) dies
    3. 0 w/ 3 lives neighbors (1s) lives turn
    '''
    conversion_map = {'#': 0, '*': 1}
    rows, cols = len(board), len(board[0])

    for row in range(rows):
        for col in range(cols):
            neighbors = self.count(board, row, col)
            if board[row][col] == 1 and (neighbors < 2 or neighbors > 3):
                board[row][col] = '#'
            elif board[row][col] == 0 and neighbors == 3:
                board[row][col] = '*'

    for row in range(rows):
        for col in range(cols):
            if board[row][col] in conversion_map:
                board[row][col] = conversion_map[board[row][col]]


def count(self, board, row, col):
    count = 0
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

    for i, j in directions:
        newRow, newCol = row + i, col + j
        if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]) and (board[newRow][newCol] == 1 or board[newRow][newCol] == "#"):
            count += 1
    return count
