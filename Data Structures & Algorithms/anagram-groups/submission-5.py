class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        for i, s in enumerate(strs):
            freq_array = [0] * 26
            for c in s:
                freq_array[ord(c) - 97] += 1
            
            freq_tuple = tuple(freq_array)    
            if freq_tuple in groups:
                groups[freq_tuple].append(i)
            else:
                groups[freq_tuple] = [i]

        lst = []
        for _, group in groups.items():
            sublst = []
            for i in group:
                sublst.append(strs[i])
            lst.append(sublst)
        
        return lst