class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        highest = 0
        for n in nums:
            if n - 1 in num_set:
                continue
            count = 1
            num = n + 1
            while num in num_set:
                num += 1
                count += 1
            
            highest = max(highest, count)
        return highest