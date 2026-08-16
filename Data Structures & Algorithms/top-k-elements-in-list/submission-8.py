class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        
        for n in nums:
            freq_map[n] += 1
        
        freq_list = [[] for _ in range(len(nums) + 1)]
        for n, freq in freq_map.items():
            freq_list[freq].append(n)
        
        print(freq_list)

        retval = []
        end = len(freq_list) - 1
        while len(retval) < k:
            retval += freq_list[end]
            end -= 1

        return retval
