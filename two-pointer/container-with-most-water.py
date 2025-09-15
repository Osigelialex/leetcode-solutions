from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        area = 0

        while L < R:
            lval, rval = height[L], height[R]
            length = min(lval, rval)
            breadth = R - L
            curr_area = length * breadth

            if curr_area > area:
                area = curr_area
            if lval < rval:
                L += 1
            else: 
                R -= 1

        return area
