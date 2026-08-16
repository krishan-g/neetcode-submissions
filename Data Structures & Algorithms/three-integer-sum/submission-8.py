class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if (i >= 1 and nums[i] == nums[i - 1]):
                continue

            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while (l < r):
                left = nums[l]
                right = nums[r]

                if (left + right == target):
                    triplets.append([-target, left, right])
                    while (l < r and nums[l] == left):
                        l += 1
                
                elif (left + right < target):
                    l += 1
                
                else:
                    r -= 1

        return triplets