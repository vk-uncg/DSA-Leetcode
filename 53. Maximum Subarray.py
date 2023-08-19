class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum+nums[i], nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum