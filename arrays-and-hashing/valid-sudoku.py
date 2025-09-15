from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rmap = defaultdict(set)
        cmap = defaultdict(set)
        smap = defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue

                sub_box = (i // 3) * 3 + (j // 3)
                if value in rmap[i] or value in cmap[j] \
                    or value in smap[sub_box]:
                    return False
   
                rmap[i].add(value)
                cmap[j].add(value)
                smap[sub_box].add(value)    
        return True
