from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        m = len(matrix)
        n = len(matrix[0])
        end = m * n - 1

        def search(start, end):
            if start > end:
                return False
            
            mid = (start + end) // 2
            row = mid // n
            col = mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value > target:
                return search(start, mid - 1)
            else:
                return search(mid + 1, end)

        return search(start, end)
