# Type: Greedy, Heap
from heapq import *


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    trips.sort(key=lambda trip: trip[1])
    minHeap = []
    current_capacity = 0

    for num, start, end in trips:
        while minHeap and start >= minHeap[0][0]:
            num_passengers = heappop(minHeap)[1]
            current_capacity -= num_passengers

        heappush(minHeap, (end, num))
        current_capacity += num
        if current_capacity > capacity:
            return False

    return True
