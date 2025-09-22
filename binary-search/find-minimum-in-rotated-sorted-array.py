from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[n - 1] > nums[0]:
            return nums[0]
        
        l, r = 1, n - 1
        top = nums[-1]

        while l <= r:
            mid = (l + r) // 2
            value = nums[mid]
            if value < nums[mid - 1]:
                return value
            elif value > top:
                l = mid + 1
            else:
                r = mid - 1
                