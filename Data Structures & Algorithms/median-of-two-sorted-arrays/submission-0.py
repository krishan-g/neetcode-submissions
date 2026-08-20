class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # A is the shortest array
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            B, A = A, B

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            A_left = A[i - 1] if i - 1 >= 0 else -float('inf')
            A_right = A[i] if i < len(A) else float('inf')

            B_left = B[j - 1] if j - 1 >= 0 else -float('inf')
            B_right = B[j] if j < len(B) else float('inf')

            if A_left > B_right:
                r = i - 1
            
            elif B_left > A_right:
                l = i + 1

            else:
                right_min = min(A_right, B_right)
                if total % 2 != 0:
                    return right_min
                else:
                    left_max = max(A_left, B_left)
                    return (left_max + right_min) / 2

