class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        for s in strs:
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c) - ord('a')] += 1
            
            anagram_map[tuple(freq_list)].append(s)
        
        res = []
        for group in anagram_map:
            res.append(anagram_map[group])
        return res