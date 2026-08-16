class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for i in range(len(strs)):
            sort_s = "".join(sorted(strs[i]))
            if sort_s in sorted_strs:
                sorted_strs[sort_s].append(i)
            else:
                sorted_strs[sort_s] = [i]
        
        groups = []
        for lst in sorted_strs:
            group = []
            for i in sorted_strs[lst]:
                group.append(strs[i])
            
            groups.append(group)

        return groups