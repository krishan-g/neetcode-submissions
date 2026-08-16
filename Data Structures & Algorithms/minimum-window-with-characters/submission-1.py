class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        t_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        
        desired_matches = len(t_map)
        matches = 0
        
        
        shortest = float('inf')

        l, r = 0, 0

        s_map = {}
        while r < len(s):
            if s[r] in t_map:
                s_map[s[r]] = s_map.get(s[r], 0) + 1
                if s_map[s[r]] == t_map[s[r]]:
                    matches += 1

            while matches == desired_matches and l < r + 1:
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    shortest_sub = s[l:r+1]

                if s[l] in t_map:
                    s_map[s[l]] -= 1
                    if s_map[s[l]] == t_map[s[l]] - 1:
                        matches -= 1
                l += 1
            
            r += 1
        
        return "" if shortest == float('inf') else shortest_sub
