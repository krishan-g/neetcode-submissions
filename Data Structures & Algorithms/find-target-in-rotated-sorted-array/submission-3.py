class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                if nums[m] >= nums[l]:  # in big section
                    if nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1
                else:                   # in small section
                    r = m - 1

            elif nums[m] < target:
                if nums[m] >= nums[l]:  # in big section
                    l = m + 1
                else:                   # in small section
                    if nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1

            else:
                return m
        
        return -1