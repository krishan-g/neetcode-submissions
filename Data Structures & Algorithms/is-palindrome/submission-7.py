class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_modified = ""
        for c in s:
            if (ord('a') <= ord(c) <= ord('z')):
                s_modified += c
            elif (ord('A') <= ord(c) <= ord('z')):
                s_modified += chr(ord(c) - ord('A') + ord('a'))
            elif (ord('0') <= ord(c) <= ord('9')):
                s_modified += c
        
        return s_modified == s_modified[::-1]