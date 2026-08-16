class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_array = [0] * 26
        l, r = 0, 0

        longest = 0
        current = 0

        while r < len(s):
            freq_array[ord(s[r]) - ord("A")] += 1
            current += 1

            highest = max(freq_array)
            if r - l + 1 - highest <= k:
                longest = max(longest, current)
                r += 1
            else:
                while r - l + 1 - max(freq_array) > k:
                    current -= 1
                    freq_array[ord(s[l]) - ord("A")] -= 1
                    l += 1
                r += 1

        
        return longest