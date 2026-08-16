class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right_prefix = [1]
        for i in range(len(nums) - 1):
            right_prefix.append(nums[i] * right_prefix[i])

        left_prefix = [1]
        nums_reverse = nums[::-1]
        for i in range(len(nums) - 1):
            left_prefix.append(nums_reverse[i] * left_prefix[i])
        left_prefix.reverse()


        print(right_prefix)
        print(left_prefix)
        return [right_prefix[i] * left_prefix[i] for i in range(len(nums))]
        

