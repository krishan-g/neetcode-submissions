class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums_sorted = sorted(set(nums))

        highest = 1
        count = 1
        for i in range(1, len(nums_sorted)):
            if (nums_sorted[i] - nums_sorted[i-1] == 1):
                count += 1
            else:
                count = 1

            highest = max(highest, count)

        return highest