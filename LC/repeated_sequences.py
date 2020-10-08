from collections import defaultdict


def findRepeatedDnaSequences(self, s: str) -> List[str]:
    hash_map = defaultdict(int)
    for i in range(len(s)-9):
        hash_map[s[i:i+10]] += 1
    return [key for key, value in hash_map.items() if value > 1]
