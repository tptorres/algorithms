def boggleBoard(board, words):
    res = []
    for word in words:
        if contains_word(board, word):
            res.append(word)
    return res


def contains_word(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if check_word(board, word, row, col):
                return True
    return False


def check_word(board, word, row, col):
    if not word:
        return True

    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) \
            or board[row][col] != word[0]:
        return False

    temp = board[row][col]
    board[row][col] = '*'
    res = check_word(board, word[1:], row-1, col) or \
        check_word(board, word[1:], row, col+1) or \
        check_word(board, word[1:], row+1, col) or \
        check_word(board, word[1:], row, col-1) or \
        check_word(board, word[1:], row-1, col) or \
        check_word(board, word[1:], row-1, col-1) or \
        check_word(board, word[1:], row-1, col+1) or \
        check_word(board, word[1:], row+1, col+1) or \
        check_word(board, word[1:], row+1, col-1)

    board[row][col] = temp
    return res
