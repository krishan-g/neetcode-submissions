class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = ""
        for s in strs:
            encoded_msg += str(len(s)) + "-" + s
        return encoded_msg

    def decode(self, s: str) -> List[str]:
        decoded_msg = []
        i = 0
        j = 0
        while j < len(s):
            i = j
            while s[j] != "-":
                j += 1
            num = int(s[i:j])
            decoded_msg.append(s[j+1:j+num+1])
            j += num + 1
        return decoded_msg

