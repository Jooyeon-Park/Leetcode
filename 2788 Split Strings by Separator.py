class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for i in words:
            output+=i.split(separator)
        output = [word for word in output if word != ""]
        return output
