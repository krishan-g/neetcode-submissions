class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_height = height[l]
        right_height = height[r]
        total = 0
        while l < r:
            if left_height < right_height:
                l += 1
                left_height = max(left_height, height[l])
                total += left_height - height[l]
            else:
                r -= 1
                right_height = max(right_height, height[r])
                total += right_height - height[r]
        return total