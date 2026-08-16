class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 0
            
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 0
        
        for letter in s_dict:
            if (letter not in t_dict) or (s_dict[letter] != t_dict[letter]):
                return False
        
        for letter in t_dict:
            if (letter not in s_dict) or (t_dict[letter] != s_dict[letter]):
                return False
        
        return True

        