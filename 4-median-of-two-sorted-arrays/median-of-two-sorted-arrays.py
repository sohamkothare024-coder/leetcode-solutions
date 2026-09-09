class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to keep binary search bounds efficient
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2   # partition point in nums1
            j = half - i            # partition point in nums2

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                high = i - 1  # move partition in nums1 left
            else:
                low = i + 1   # move partition in nums1 right

        raise ValueError("Input arrays are not sorted")