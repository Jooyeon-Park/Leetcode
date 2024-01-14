class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        #shortest string in the list
        shortestLength = 201
        index = 0
        for k in range(0,len(strs)):
            if len(strs[k]) < shortestLength:
                shortestLength = len(strs[k])
                index = k

        for i in range (shortestLength,0,-1): # Length of prefix
            common = True
            for j in range(0, len(strs)): # compare it to other ones in strs
                if strs[index][:i] != strs[j][:i]:
                    common = False
                    break
            if common:
                return strs[index][:i]
        return ""