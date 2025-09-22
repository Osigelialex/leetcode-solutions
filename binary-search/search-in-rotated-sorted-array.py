from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, n - 1

        top = nums[-1]
        while l <= r:
            mid = (l + r) // 2
            value = nums[mid]

            if value == target:
                return mid
            elif value < target:
                if target > top and value < top:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < top and value < top:
                    r = mid - 1
                elif target > top and value > top:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
