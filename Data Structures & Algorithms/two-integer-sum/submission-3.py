class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if other in num_to_index:
                return [num_to_index[other], i]
            num_to_index[nums[i]] = i