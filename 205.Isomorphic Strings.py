class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        i = 0
        while i < len(s):
            if t[i] in t_s:
                if t_s[t[i]] != s[i]:
                    return False
            else:
                if s[i] in s_t:
                    return False
                
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
            i += 1
        return True