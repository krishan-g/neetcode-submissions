class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s))
            encoded += "-"
            encoded += s
            
        return encoded

    def decode(self, s: str) -> List[str]:
        
        if len(s) == 0:
            return []
        
        decoded = []
        
        left = 0
        right = 0
        while (left < len(s)):
            while (s[right] != "-"):
                right += 1
            size = int(s[left:right])
            decoded.append(s[right + 1: right + size + 1])
            left = right + size + 1
            right = left
        
        return decoded
