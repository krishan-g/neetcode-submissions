class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}
        highest = 0

        for n in nums:
            
            if n in length:
                continue
            
            if (n - 1 in length and n + 1 in length):
                length[n] = length[n - 1] + length[n + 1] + 1
            elif (n - 1 in length):
                length[n] = length[n - 1] + 1
            elif (n + 1 in length):
                length[n] = length[n + 1] + 1
            else:
                length[n] = 1
            
            prev_val = n - 1
            while (prev_val in length):
                length[prev_val] = length[n]
                prev_val -= 1
            
            next_val = n + 1
            while (next_val in length):
                length[next_val] = length[n]
                next_val += 1
                
            highest = max(highest, length[n])
        
        return highest