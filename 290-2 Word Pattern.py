class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_s = {}
        s_p = {}

        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            print(f"pattern[i]: {pattern[i]}, s[i]: {s[i]}")
            if pattern[i] in p_s:
                if p_s[pattern[i]] != s[i]:
                    return False
                if s[i] in s_p and s_p[s[i]] == pattern[i]:
                    continue
                else:
                    return False
            else:
                if s[i] in s_p:
                        return False
                else:
                    s_p[s[i]] = pattern[i]
                    p_s[pattern[i]] = s[i]
            print(f"p_s: {p_s}, s_p: {s_p}")

        
        return True