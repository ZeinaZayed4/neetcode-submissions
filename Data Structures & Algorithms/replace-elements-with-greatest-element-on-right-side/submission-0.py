class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range (len(arr) - 1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr
