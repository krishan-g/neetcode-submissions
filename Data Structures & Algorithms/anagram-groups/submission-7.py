class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist_map = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in sublist_map:
                sublist_map[sorted_s].append(s)
            else:
                sublist_map[sorted_s] = [s]
        
        group = []
        for sublist in sublist_map.values():
            group.append(sublist)
        
        return group