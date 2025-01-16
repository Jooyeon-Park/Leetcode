class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort first
        citations.sort(reverse = True)

        h = 0
        for i in range(0,len(citations)):
            if citations[i] > h:
                h = i+1
        return h