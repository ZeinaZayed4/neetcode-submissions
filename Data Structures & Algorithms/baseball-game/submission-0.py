class Solution:
    def calPoints(self, operations: list[str]) -> int:
        results = []
        total = 0

        for op in operations:
            if op == "+":
                result = results[-1] + results[-2]
                total += result
                results.append(result)
            elif op == "D":
                result = results[-1] * 2
                total += result
                results.append(result)
            elif op == "C":
                total -= results.pop()
            else:
                value = int(op)
                total += value
                results.append(value)
        
        return total
