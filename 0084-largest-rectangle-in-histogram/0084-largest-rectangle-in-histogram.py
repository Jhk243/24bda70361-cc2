from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # store indices of bars in increasing height order
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area