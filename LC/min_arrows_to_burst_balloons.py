# Type: Greedy, Interval


def findMinArrowShots(self, points: List[List[int]]) -> int:
    if not points:
        return 0
    if len(points) == 1:
        return 1
    points.sort(key=lambda point: point[0])
    arrows = 0
    start = points[0][0]
    end = points[0][1]

    for current_start, current_end in points:
        if current_start <= end:
            start = max(current_start, start)
            end = min(current_end, end)
        else:
            arrows += 1
            start = current_start
            end = current_end

    return arrows + 1
