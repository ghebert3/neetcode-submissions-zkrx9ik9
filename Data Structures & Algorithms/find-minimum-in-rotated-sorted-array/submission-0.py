class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        r = n - 1

        while L < r:
            m = (L + r) // 2

            if nums[m] > nums[r]:
                L = m + 1
            else:
                r = m
        return nums[L]
        