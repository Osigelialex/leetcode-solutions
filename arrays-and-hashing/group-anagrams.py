from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in map:
                map[sorted_str].append(i)
            else:
                map[sorted_str] = [i]
        
        return list(map.values())