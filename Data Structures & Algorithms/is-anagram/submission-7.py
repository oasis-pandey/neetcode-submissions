class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in s_set:
                s_set[i] = s_set[i] + 1
            else:
                s_set[i] = 1

        for i in t:
            if i in t_set:
                t_set[i] = t_set[i] + 1
            else:
                t_set[i] = 1
        
        for i in s_set:
            if s_set[i] not in t_set or (s_set[i] != t_set[i]):
                return False
            else:
                return True

        
            
        