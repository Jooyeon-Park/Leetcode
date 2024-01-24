class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_s = {}
        s_pattern = {}
        sList = s.split(" ")

        if len(pattern) != len(sList):
            return False
        
        for char_p, char_s in zip(pattern, sList):
            if char_p in pattern_s and pattern_s[char_p] != char_s:
                return False
            else:
                pattern_s[char_p] = char_s
            if char_s in s_pattern and s_pattern[char_s] != char_p:
                return False
            else:
                s_pattern[char_s] = char_p
        return True