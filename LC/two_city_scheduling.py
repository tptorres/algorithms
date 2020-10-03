def two_city_scheduling(costs):
    costs.sort(key=lambda cost: cost[0] - cost[1])
    res = 0

    for i in range(len(costs) // 2):
        res += costs[i][0] + costs[i + len(costs) // 2][1]
    return res


print(two_city_scheduling([[10, 20], [30, 200], [400, 50], [30, 20]]))
