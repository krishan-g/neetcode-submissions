class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if (i >= 1 and sorted_nums[i] == sorted_nums[i - 1]):
                continue

            target = -sorted_nums[i]
            l, r = i + 1, len(nums) - 1

            while (l < r):
                left = sorted_nums[l]
                right = sorted_nums[r]

                if (left + right == target):
                    triplets.append([-target, left, right])
                    while (l < r and sorted_nums[l] == left):
                        l += 1
                
                elif (left + right < target):
                    l += 1
                
                else:
                    r -= 1

        return triplets