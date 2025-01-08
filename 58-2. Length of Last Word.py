class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        isWord = False
        for i in reversed(s):
            if i == " " and not isWord:
                continue
            if i != " " and isWord:
                count += 1
            if i != " " and not isWord:
                isWord = True
                count += 1
            if i == " " and isWord:
                return count
        return count
            