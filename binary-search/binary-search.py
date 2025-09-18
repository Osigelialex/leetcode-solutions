from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        if n == 1 and nums[0] == target:
            return 0

        while l <= r:
            mid = (l + r) // 2
            value = nums[mid]
            
            if value == target:
                return mid
            elif value > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return - 1