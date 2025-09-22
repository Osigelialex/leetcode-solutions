from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)
        candidates = []

        if h == n:
            return r
        
        if n == 1:
            return ceil(piles[0] / h)

        while l <= r:
            mid = (l + r) // 2
            total = 0
            
            for i in piles:
                total += ceil(i / mid)

            if total <= h:
                candidates.append(mid)
                r = mid - 1
            else:
                l = mid + 1

        return candidates[-1]