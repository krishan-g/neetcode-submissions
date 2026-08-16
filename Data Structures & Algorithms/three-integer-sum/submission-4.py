class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            
            l = i + 1
            r = len(sorted_nums) - 1
            target = -sorted_nums[i]
            while l < r:

                if (sorted_nums[l] + sorted_nums[r] == target):
                    triplets.add((sorted_nums[i], 
                                    sorted_nums[l], 
                                    sorted_nums[r]))
                    l += 1
                elif (sorted_nums[l] + sorted_nums[r] < target):
                    l += 1
                else:
                    r -= 1


        return [list(group) for group in triplets]