class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        j = 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
            i += 1

            if j >= len(s):
                return True
        return False

                