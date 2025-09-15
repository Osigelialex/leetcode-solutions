from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        if N <= 1:
            return N
        
        map = {}
        for i in range(N):
            map[position[i]] = speed[i]
    
        position.sort()
        count = 0
        stack = []

        for i in range(N - 1, -1, -1):
            curr = position[i]
            time = (target - curr) / map[curr]
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack = []
                count += 1
                stack.append(time)
        
        return count + 1 if stack else count