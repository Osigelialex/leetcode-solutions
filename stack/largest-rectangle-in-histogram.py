from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        N = len(heights)
        left_boundaries = [-1] * N
        right_boundaries = [N] * N

        for i in range(N):
            while stack and heights[i] < heights[stack[-1]]:
                right_boundaries[stack.pop()] = i
            stack.append(i)
    
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left_boundaries[stack.pop()] = i
            stack.append(i)
        
        for j in range(N):
            area = heights[j] * (right_boundaries[j] - left_boundaries[j] - 1)
            if area > max_area:
                max_area = area

        return max_area