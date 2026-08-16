class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] # 1, 1, 2, 8
        right_prod = [1] # 1, 6, 24, 48
        
        left_prefix = 1
        for i in range(len(nums) - 1):
            left_prod.append(left_prefix * nums[i])
            left_prefix *= nums[i]

        right_prefix = 1
        for j in range(len(nums) - 1, 0, -1):
            right_prod.append(right_prefix * nums[j])
            right_prefix *= nums[j]

        res = [left_prod[i] * right_prod[-i-1] for i in range(len(nums))]
        return res