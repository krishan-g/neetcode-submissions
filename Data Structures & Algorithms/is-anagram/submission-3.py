class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_freq_map = {}
        for s_letter in s:
            s_freq_map[s_letter] = s_freq_map.get(s_letter, 0) + 1
        
        t_freq_map = {}
        for t_letter in t:
            t_freq_map[t_letter] = t_freq_map.get(t_letter, 0) + 1

        for letter in s_freq_map:
            if letter not in t_freq_map:
                return False
            if s_freq_map[letter] != t_freq_map[letter]:
                return False

        return True        