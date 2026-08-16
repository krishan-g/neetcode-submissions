# Optimal Solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        
        count_to_values = [[] for i in range(len(nums))]

        for key, val in freq_map.items():
            count_to_values[val - 1].append(key)
        
        ans = []
        for i in range(len(count_to_values) - 1, -1, -1):
            ans += count_to_values[i]
            if len(ans) == k:
                return ans