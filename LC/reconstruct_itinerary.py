from heapq import *
from collections import defaultdict


def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    res = []
    for u, v in tickets:
        if u not in graph:
            graph[u] = []
        heappush(graph[u], v)

    self.helper("JFK", graph, res)
    return res[::-1]


def helper(self, airport, graph, res):
    if airport in graph:
        while graph[airport]:
            node = heappop(graph[airport])
            self.helper(node, graph, res)
    res.append(airport)
