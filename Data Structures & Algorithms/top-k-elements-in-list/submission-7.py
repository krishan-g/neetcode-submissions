class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        
        count_list = [[] for _ in range(len(nums) + 1)]
        for n, count in freq_map.items():
            count_list[count].append(n)
        
        res = []
        for i in range(len(count_list) - 1, 0, -1):
            for n in count_list[i]:
                res.append(n)
                if len(res) == k:
                    return res