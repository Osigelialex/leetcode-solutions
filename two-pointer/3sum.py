from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            curr = nums[i]
            if i > 0 and nums[i - 1] > 0:
                break

            if i > 0 and curr == nums[i - 1]:
                continue

            target = -curr
            L = i + 1
            R = len(nums) - 1

            while L < R:
                lcurr, rcurr = nums[L], nums[R]
                total = lcurr + rcurr
                if total == target:
                    res.append([curr, lcurr, rcurr])
                    while nums[L] == lcurr and L < R:
                        L += 1
                    while nums[R] == rcurr and R > L:
                        R -= 1
                elif total > target:
                    R -= 1
                else:
                    L += 1

        return res