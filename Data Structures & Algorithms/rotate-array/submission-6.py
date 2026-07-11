class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
        n = len(nums)
        reverse(0, n-1)
        reverse(0, (k%n)- 1)
        reverse(k%n, len(nums)-1)