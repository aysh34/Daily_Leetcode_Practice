class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAlt, maxAlt = 0, 0
        for g in gain:
            currentAlt += g
            if currentAlt > maxAlt:
                maxAlt = currentAlt
        return maxAlt
