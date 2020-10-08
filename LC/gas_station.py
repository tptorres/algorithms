def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    gas_left = gas_needed = start = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        gas_left += g - c
        if gas_left < 0:
            gas_needed -= gas_left
            start = i + 1
            gas_left = 0
    return start if gas_left >= gas_needed else -1
