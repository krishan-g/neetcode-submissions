class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1



        l, r = 0, len(s1) - 1

        while r < len(s2):
            s2_map = {}
            for i in range(l, r + 1):
                s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

                if s2_map[s2[i]] > s1_map.get(s2[i], 0):
                    l += 1
                    r += 1
                    break
                else:
                    if i == r:
                        return True

        
        return False
