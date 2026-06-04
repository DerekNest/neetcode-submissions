class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right-left) // 2
            totalH = 0

            for pile in piles:
                totalH += math.ceil(pile / mid)
            if totalH <= h:
                right = mid
            else:
                left = mid +1
            
        return left
