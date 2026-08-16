class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if mid >= len(nums) - 1:
                break

            if nums[mid] < nums[mid + 1]:
                if nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return nums[mid + 1]
            
        return nums[0]