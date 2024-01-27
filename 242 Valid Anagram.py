class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        
        for char in t:
            if char in dic:
                dic[char] -= 1
                if dic[char] == 0:
                    dic.pop(char)
            else:
                return False
        if len(dic.keys()) != 0:
            return False
        
        return True 