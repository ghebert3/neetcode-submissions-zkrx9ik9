class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R =  n - 1

        while L < R:
            m = (L+R) // 2
            if nums[m] > nums[R]:
                L = m + 1
            else:
                R = m
        return nums[L]