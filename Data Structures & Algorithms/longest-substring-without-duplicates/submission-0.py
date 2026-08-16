class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0

        characters = set()
        longest = 0
        current = 0
        while (left < len(s) and right < len(s)):
            if s[right] in characters:
                characters.remove(s[left])
                left += 1
                current -= 1
            else:
                characters.add(s[right])
                right += 1
                current += 1
                longest = max(longest, current)
        
        return longest
