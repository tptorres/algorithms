from collections import deque


def rotten_oranges(grid):
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    rotten = deque()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rotten.append((row, col))
            elif grid[row][col] == 1:
                fresh += 1
    res = 0
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while rotten and fresh > 0:
        res += 1
        sz = len(rotten)

        for _ in range(sz):
            row, col = rotten.popleft()

            for x, y in directions:
                newRow, newCol = row + x, col + y
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                    rotten.append((newRow, newCol))
                    grid[newRow][newCol] = 2
                    fresh -= 1
    return res if fresh == 0 else -1


print(rotten_oranges([[2, 1, 1], [1, 1, 2], [0, 1, 1]]))
