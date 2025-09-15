from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in map:
                return map[complement], i
            else:
                map[current] = i
        return None