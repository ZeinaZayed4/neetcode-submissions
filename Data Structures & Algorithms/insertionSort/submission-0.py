# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        res = []
        for i in range(len(pairs)):
            cur = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > cur.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = cur
            res.append(pairs[:])
        
        return res
