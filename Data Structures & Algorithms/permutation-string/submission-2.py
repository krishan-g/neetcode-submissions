from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            if Counter(s2[i:i+len(s1)]) == s1_map:
                return True
        
        return False