class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        highest = 0

        for i, h in enumerate(heights):
            old_i = i
            while stack and h < stack[-1][1]:
                old_i, old_h = stack.pop()
                highest = max(highest, (i - old_i) * old_h)
            stack.append((old_i, h))
        
        for i, h in stack:
            highest = max(highest, (len(heights) - i) * h)
        
        return highest