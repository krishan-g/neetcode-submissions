class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        ans = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)

        return ans[:k]