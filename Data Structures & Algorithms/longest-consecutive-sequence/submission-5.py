class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        highest = 0
        length_map = {}

        for n in set(nums):

            if n - 1 in length_map and n + 1 in length_map:
                length = length_map[n - 1] + length_map[n + 1] + 1
                length_map[n] = length
                length_map[n - length_map[n - 1]] = length
                length_map[n + length_map[n + 1]] = length
                highest = max(highest, length)

            elif n - 1 in length_map:
                length = length_map[n - 1] + 1
                length_map[n] = length
                length_map[n - length_map[n - 1]] = length
                highest = max(highest, length)

            elif n + 1 in length_map:
                length = length_map[n + 1] + 1
                length_map[n] = length
                length_map[n + length_map[n + 1]] = length
                highest = max(highest, length)

            else:
                length = 1
                length_map[n] = length
                highest = max(highest, length)
        
        return highest
