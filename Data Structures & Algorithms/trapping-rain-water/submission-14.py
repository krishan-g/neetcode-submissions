class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0
        trapped = 0

        l, r = 0, len(height) - 1
        left_highest = height[l]
        right_highest = height[r]

        while l < r:
            if left_highest <= right_highest:
                l += 1
                while height[l] < left_highest:
                    trapped += left_highest - height[l]
                    l += 1
                left_highest = height[l]
            
            else:
                r -= 1
                while height[r] < right_highest:
                    trapped += right_highest - height[r]
                    r -= 1
                right_highest = height[r]

            total += trapped
            trapped = 0

        return total    