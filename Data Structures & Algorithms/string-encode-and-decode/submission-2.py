class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            hash_index = s.find("#", i)
            str_len = int(s[i:hash_index])
            res.append(s[hash_index + 1 : hash_index+str_len + 1])
            i = hash_index+str_len + 1
        return res
            
