class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound = self.minHoursEating([sum(piles)], h)
        upperBound = max(piles)
    
        while lowerBound < upperBound:
            middle = lowerBound + (upperBound - lowerBound) // 2

            if self.minHoursEating(piles, middle) <= h:
                upperBound = middle
            else:
                lowerBound = middle + 1
        
        return lowerBound
    
    def minHoursEating(self, piles: List[int], k: int) -> int:
        total = 0
        for num in piles:
            if num % k == 0:
                total += num // k
            else:
                total += num // k + 1
        return total    