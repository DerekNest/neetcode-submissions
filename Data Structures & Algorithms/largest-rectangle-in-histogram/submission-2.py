class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)

        for i in range(n):

            while stack and heights[i] < heights[stack[-1]]:
                top_index = stack.pop()
                height = heights[top_index]


                if not stack:
                    width = i
                else: 
                    width = i - stack[-1] -1

                max_area = max(max_area, height*width)

            stack.append(i)

        while stack:
            top_index = stack.pop()
            height = heights[top_index]

            if not stack:
                width = n
            else: 
                width = n - stack[-1] -1
            
            max_area = max(max_area, height * width)
        return max_area