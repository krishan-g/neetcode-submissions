class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}
        highest = 0

        for n in nums:
            
            if n in length:
                continue
            
            left = length.get(n - 1, 0)
            right = length.get(n + 1, 0)
            total = left + right + 1

            length[n] = total
            length[n - left] = total
            length[n + right] = total
                
            highest = max(highest, total)
        
        return highest