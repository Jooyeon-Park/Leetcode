class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        elements = {}
        
        for end in range(len(s)):
            # If character is already in window, update start
            if s[end] in elements and elements[s[end]] >= start:
                start = elements[s[end]] + 1
            
            # Update character position and max length
            elements[s[end]] = end
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength