from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        soln = [1] * n     
        left_products = [1] * n
        right_products = [1] * n

        curr_prod = 1
        for i in range(1, n):
            curr_prod = nums[i - 1] * curr_prod
            left_products[i] = curr_prod
        
        curr_prod = 1
        for i in range(n - 2, -1, -1):
            curr_prod = nums[i + 1] * curr_prod
            right_products[i] = curr_prod
        
        for j in range(n):
            soln[j] = left_products[j] * right_products[j]
        
        return soln