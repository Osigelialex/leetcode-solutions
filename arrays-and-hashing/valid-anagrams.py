class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(s)):
            if s[i] in map1:
                map1[s[i]] = map1[s[i]] + 1
            else:
                map1[s[i]] = 1

            if t[i] in map2:
                map2[t[i]] = map2[t[i]] + 1
            else:
                map2[t[i]] = 1
        
        if map1 != map2:
            return False

        return True