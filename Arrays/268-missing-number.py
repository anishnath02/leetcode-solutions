class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedRange = range(len(nums)+1)
        return sum(expectedRange) - sum(nums)
