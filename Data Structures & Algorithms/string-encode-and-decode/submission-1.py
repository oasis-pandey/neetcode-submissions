class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) != 0:
            str_len = 0
            hash_index = s.find("#")
            str_len = int(s[:hash_index])
            res.append(s[hash_index + 1 : hash_index+str_len + 1])
            s = s[hash_index+str_len+1:]
        return res
            
