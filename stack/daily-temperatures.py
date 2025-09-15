from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        soln = [0] * N

        for i, curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                prev = stack.pop()
                soln[prev] = i - prev
            stack.append(i)
        return soln