class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for i in magazine:
            if mag.get(i) is not None:
                mag[i] += 1
            else:
                mag[i] = 1
        
        for j in ransomNote:
            if mag.get(j) is None or mag.get(j) <= 0:
                return False
            mag[j] -= 1
        return True