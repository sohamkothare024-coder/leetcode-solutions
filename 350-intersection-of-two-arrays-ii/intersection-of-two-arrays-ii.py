class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        result = []
        for num in c1:
            if num in c2:
                result.extend([num] * min(c1[num], c2[num]))
        return result