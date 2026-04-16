class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) -1
        maxVol = 0

        for i in range(last+1):
            currVol = min(heights[first],  heights[last]) * (last-first)

            if currVol > maxVol:
                maxVol = currVol
            
            if heights[first] < heights[last]:
                first +=1
            else:
                last -=1

        return maxVol
        