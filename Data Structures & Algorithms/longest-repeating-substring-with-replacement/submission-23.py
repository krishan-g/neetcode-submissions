class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        freq_array = [0] * 26


        for r in range(len(s)):
            freq_array[ord(s[r]) - ord("A")] += 1

            while r - l + 1 - max(freq_array) > k:
                freq_array[ord(s[l]) - ord("A")] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

