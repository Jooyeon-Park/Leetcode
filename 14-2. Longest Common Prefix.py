class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for word in strs:
            if len(word) < len(shortest):
                shortest = word
        
        pre = ""
        for i in range(0,len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return pre
            pre += word[i]
        
        return pre