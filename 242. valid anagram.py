class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for j in t:
            if j in dic:
                dic[j] -= 1
                if dic[j] == 0:
                    dic.pop(j)
            else:
                return False

        if len(dic.keys()) == 0:
            return True    
        else:
            return False