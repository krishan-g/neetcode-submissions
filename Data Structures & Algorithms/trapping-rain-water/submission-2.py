class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_high = height[left]
        right_high = height[right]

        total = 0
        while left < right:
            # 1 5 left, right
            # 0 0 left_high, right_high
            # 0   total

            if height[left] < height[right]:
                left += 1
                if height[left] < left_high:
                    total += left_high - height[left]
                else:
                    left_high = height[left]

            else:
                right -= 1
                if height[right] < right_high:
                    total += right_high - height[right]
                else:
                    right_high = height[right]
            
        return total

