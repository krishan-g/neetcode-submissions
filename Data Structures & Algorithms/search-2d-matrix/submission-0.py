class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        left, right = 0, len(matrix) * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            r = mid // cols
            c = mid % cols

            if target > matrix[r][c]:
                left = mid + 1
            elif target < matrix[r][c]:
                right = mid - 1
            else:
                return True
        
        return False