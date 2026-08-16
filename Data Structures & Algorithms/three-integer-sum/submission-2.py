class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)

        lst = []
        for i in range(len(sorted_nums) - 2):
            
            if i >= 1 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            curr = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1
            target = -1 * curr
    

            while (left < right):
                if sorted_nums[left] + sorted_nums[right] == target:
                    fst = sorted_nums[left]
                    snd = sorted_nums[right]
                    
                    lst.append([curr, fst, snd])
                    while (sorted_nums[left] == fst and left < right):
                        left += 1
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                else:
                    right -= 1
            
        return lst
                